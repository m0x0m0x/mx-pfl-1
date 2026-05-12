# Deleting the Upstash Entries

---

1. [Deleting the Upstash Entries](#deleting-the-upstash-entries)
   1. [**How to Open Upstash Web CLI:**](#how-to-open-upstash-web-cli)
   2. [**Delete Commands for Upstash Web CLI:**](#delete-commands-for-upstash-web-cli)
      1. [**1. Delete ALL Keys (Nuclear Option):**](#1-delete-all-keys-nuclear-option)
      2. [**2. Delete Only Keys with a Pattern:**](#2-delete-only-keys-with-a-pattern)
      3. [**3. Delete Specific Keys One by One:**](#3-delete-specific-keys-one-by-one)
      4. [**4. Delete by TTL (Expired Keys Cleanup):**](#4-delete-by-ttl-expired-keys-cleanup)
   3. [**Most Useful for Your Situation:**](#most-useful-for-your-situation)
      1. [**Clear ALL Flask-Limiter Keys (Keep everything else):**](#clear-all-flask-limiter-keys-keep-everything-else)
      2. [**Clear Keys for a Specific IP:**](#clear-keys-for-a-specific-ip)
      3. [**Clear Keys for a Specific Endpoint:**](#clear-keys-for-a-specific-endpoint)
   4. [**Safety Commands (Test First):**](#safety-commands-test-first)
      1. [**Count how many keys will be deleted:**](#count-how-many-keys-will-be-deleted)
      2. [**Preview before deleting:**](#preview-before-deleting)
   5. [**Complete Example Session:**](#complete-example-session)
   6. [**Pro Tips:**](#pro-tips)
   7. [**Quick Reference Card:**](#quick-reference-card)

---

Perfect! The Upstash Web CLI is the easiest way. Here's how to delete keys using it:

## **How to Open Upstash Web CLI:**

1. Go to your Upstash Console
2. Click on your database (`mx-pfl-1-pfla-p5-flask-limiter`)
3. Click the **"CLI"** tab (next to Data Browser)
4. A terminal window opens - you're ready!

## **Delete Commands for Upstash Web CLI:**

### **1. Delete ALL Keys (Nuclear Option):**

```redis
FLUSHALL
```

⚠️ **Warning:** Deletes EVERYTHING in this Redis instance across all apps

### **2. Delete Only Keys with a Pattern:**

```redis
# Delete all rate limiter keys
EVAL "return redis.call('DEL', unpack(redis.call('KEYS', ARGV[1])))" 0 "limiter:*"

# Delete all Flask app keys
EVAL "return redis.call('DEL', unpack(redis.call('KEYS', ARGV[1])))" 0 "LIMITS:LIMITER:*"

# Delete all debug route keys
EVAL "return redis.call('DEL', unpack(redis.call('KEYS', ARGV[1])))" 0 "*debug*"
```

### **3. Delete Specific Keys One by One:**

```redis
# See what keys exist first
KEYS *

# Delete specific keys
DEL "LIMITS:LIMITER/103.216.213.17/main.home/100/1/day"
DEL "LIMITS:LIMITER/108.171.108.178/main.home/100/1/day"
```

### **4. Delete by TTL (Expired Keys Cleanup):**

```redis
# Delete all keys with TTL = -1 (no expiry)
EVAL "local keys = redis.call('KEYS', ARGV[1]); for i=1,#keys do if redis.call('TTL', keys[i]) == -1 then redis.call('DEL', keys[i]) end end return #keys" 0 "*"
```

## **Most Useful for Your Situation:**

### **Clear ALL Flask-Limiter Keys (Keep everything else):**

```redis
EVAL "local keys = redis.call('KEYS', 'LIMITS:LIMITER:*'); if #keys > 0 then return redis.call('DEL', unpack(keys)) else return 0 end" 0
```

### **Clear Keys for a Specific IP:**

```redis
EVAL "local keys = redis.call('KEYS', '*103.216.213.17*'); if #keys > 0 then return redis.call('DEL', unpack(keys)) else return 0 end" 0
```

### **Clear Keys for a Specific Endpoint:**

```redis
EVAL "local keys = redis.call('KEYS', '*main.home*'); if #keys > 0 then return redis.call('DEL', unpack(keys)) else return 0 end" 0
```

## **Safety Commands (Test First):**

### **Count how many keys will be deleted:**

```redis
# Count all rate limiter keys
KEYS LIMITS:LIMITER:* | LEN

# Count keys for specific IP
KEYS *103.216.213.17* | LEN
```

### **Preview before deleting:**

```redis
# See all keys to be deleted
KEYS LIMITS:LIMITER:*
```

## **Complete Example Session:**

```redis
# 1. See what's there
> KEYS LIMITS:LIMITER:*
1) "LIMITS:LIMITER/103.216.213.17/main.home/100/1/day"
2) "LIMITS:LIMITER/103.216.213.17/debug.check_redis/100/1/day"
3) "LIMITS:LIMITER/108.171.108.178/main.home/100/1/day"

# 2. Count them
> KEYS LIMITS:LIMITER:* | LEN
(integer) 3

# 3. Delete them
> EVAL "local keys = redis.call('KEYS', 'LIMITS:LIMITER:*'); if #keys > 0 then return redis.call('DEL', unpack(keys)) else return 0 end" 0
(integer) 3

# 4. Verify they're gone
> KEYS LIMITS:LIMITER:*
(empty array)
```

## **Pro Tips:**

| Tip                         | Why                                        |
| --------------------------- | ------------------------------------------ |
| **Test with `KEYS` first**  | See what you're about to delete            |
| **Use patterns carefully**  | `*debug*` might delete more than expected  |
| **`FLUSHALL` is permanent** | No undo button on this one!                |
| **EVAL scripts are atomic** | Deletes all matching keys in one operation |

## **Quick Reference Card:**

```redis
# View all keys
KEYS *

# Delete everything (dangerous!)
FLUSHALL

# Delete all rate limiter keys (safest)
EVAL "local keys = redis.call('KEYS', 'LIMITS:LIMITER:*'); if #keys > 0 then return redis.call('DEL', unpack(keys)) else return 0 end" 0

# Delete by IP pattern
EVAL "local keys = redis.call('KEYS', '*103.216.213.17*'); if #keys > 0 then return redis.call('DEL', unpack(keys)) else return 0 end" 0
```

**That's it!** The Upstash Web CLI is powerful and immediate. Just be careful with `FLUSHALL` - there's no confirmation dialog! 🔥
