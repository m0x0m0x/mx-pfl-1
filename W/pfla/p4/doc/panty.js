// -------------------------------------------------------
// NOte these are needed when doing interactions with the api
// Then these functions will become useful
// -------------------------------------------------------

async function testHelloCard() {
  const responseDiv = document.getElementById('hello-response')
  const output = document.getElementById('hello-output')

  responseDiv.style.display = 'block'
  output.textContent = '⏳ Sending POST request...'

  try {
    const response = await fetch('https://ftut1.vercel.app/hello', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })

    const text = await response.text()
    output.innerHTML = text
  } catch (error) {
    output.textContent = '❌ Error: ' + error.message
  }
}

// For Card 8 - /hellopg (GET, POST, PUT)
async function testHellopg(method) {
  const responseDiv = document.getElementById('hellopg-response')
  const output = document.getElementById('hellopg-output')

  responseDiv.style.display = 'block'
  output.textContent = `⏳ Sending ${method} request...`

  try {
    const response = await fetch('https://ftut1.vercel.app/hellopg', {
      method: method,
      headers: {
        'Content-Type': 'application/json',
      },
    })

    const text = await response.text()
    output.innerHTML = text
  } catch (error) {
    output.textContent = '❌ Error: ' + error.message
  }
}
