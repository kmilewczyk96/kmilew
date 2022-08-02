'use strict';

const prepareTagBarAnimation = function () {
  const tagBars = document.getElementsByClassName('project-tag-bar');
  for (let i = 0; i < tagBars.length; i++) {
    const tagBar = tagBars[i];
    const tagBarScroll = tagBar.scrollWidth;
    if (tagBarScroll > tagBar.offsetWidth) {
      const hiddenTags = tagBar.getElementsByTagName('li');
      for (let i = 0; i < hiddenTags.length; i++) {
        // Source of the extra 10px is pagination of tag elements.
        const myAnimation = [{transform: `translateX(-${tagBarScroll + 10}px)`}];
        const myAnimationTiming = {duration: tagBarScroll * 30, iterations: Infinity};
        hiddenTags[i].animate(myAnimation, myAnimationTiming)
        hiddenTags[i].classList.remove('hidden');
      }
    }
  }
};

window.addEventListener('load', prepareTagBarAnimation);