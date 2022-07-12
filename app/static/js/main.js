'use strict';

// Smooth scrolling:
const links = document.getElementsByTagName('a');

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
