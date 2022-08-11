'use strict';

// Smooth scrolling:
const links = document.getElementsByTagName('a');
const messages = document.getElementsByClassName('messages')[0];


if (window.location.hash) {
  const hashPart = window.location.hash
  history.replaceState('', document.title, window.location.origin + window.location.pathname);
  const section = document.querySelector(hashPart);
  section.scrollIntoView();
}

for (let i = 0; i < links.length; i++) {
  links[i].addEventListener('click', function (e) {
    const hrefAtt = links[i].getAttribute('href');
    if (hrefAtt.startsWith('#')) {
      e.preventDefault()
      if (hrefAtt === '#') window.scrollTo(
        {
          top: 0,
          behavior: "smooth"
        }
      )
      else {
        const section = document.querySelector(hrefAtt);
        section.scrollIntoView(
          {
            behavior: "smooth"
          }
        );
      }
    }
  })
}

if (messages) {
  const myAnimation = [{opacity: '0'}];
  const myAnimationTiming = {duration: 2000, fill: 'forwards', delay: 1500};
  messages.animate(myAnimation, myAnimationTiming);
  Promise.all(
    messages.getAnimations().map((myAnimation) => myAnimation.finished)
  ).then(() => messages.remove());
}