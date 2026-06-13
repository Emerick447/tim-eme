let topDelta = 1
let leftDelta = 1

const screen = document.querySelector('.screen')
const logo = document.querySelector('.logo')

setInterval(() => {
  const currentTop = parseInt(logo.style.top) || 0
  const currentLeft = parseInt(logo.style.left) || 0
  const currentRight = currentLeft + logo.clientWidth
  const currentBottom = currentTop + logo.clientHeight

  if (currentBottom >= screen.clientHeight) {
    topDelta = -1
  }

  if (currentTop <= 0) {
    topDelta = 1
  }

  if (currentRight >= screen.clientWidth) {
    leftDelta = -1
  }

  if (currentLeft <= 0) {
    leftDelta = 1
  }

  logo.style.top = currentTop + topDelta + 'px'
  logo.style.left = currentLeft + leftDelta + 'px'
}, 5)