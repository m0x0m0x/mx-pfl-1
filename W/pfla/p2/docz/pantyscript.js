async function testHelloCard() {
  const responseDiv = document.getElementById('hello-response')
  const output = document.getElementById('hello-output')

  responseDiv.style.display = 'block'
  output.textContent = '⏳ Fetching...'

  try {
    const response = await fetch('https://ftut1.vercel.app/hello', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })

    const text = await response.text()
    output.textContent = text
  } catch (error) {
    output.textContent = '❌ Error: ' + error.message
  }
}
