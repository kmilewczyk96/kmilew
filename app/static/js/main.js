'use strict';

// Smooth scrolling:
const links = document.getElementsByTagName('a');

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
