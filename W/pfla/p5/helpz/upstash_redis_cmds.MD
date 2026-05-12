# Deleting the Upstash Entries

---

1. [Deleting the Upstash Entries](#deleting-the-upstash-entries)
   1. [**Pro Tips:**](#pro-tips)
   2. [**Quick Reference Card:**](#quick-reference-card)

---

Perfect! The Upstash Web CLI is the easiest way. Here's how to delete keys using it:

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
