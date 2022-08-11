'use strict';

const tagBars = document.getElementsByClassName('project-tag-bar');
const prepareTagBarAnimation = function () {
  const remToPixel = parseFloat(getComputedStyle(document.documentElement).fontSize);
  for (let i = 0; i < tagBars.length; i++) {
    const tagBar = tagBars[i];
    const tagBarScroll = tagBar.scrollWidth;
    const hiddenTags = tagBar.getElementsByClassName('hidden-tag');
    if (tagBarScroll > tagBar.offsetWidth) {
      for (let i = 0; i < hiddenTags.length; i++) {
        // Source of the extra 10px is pagination of tag elements.
        hiddenTags[i].classList.remove('hidden');
      }
      const myAnimation = [{transform: `translate3d(-${tagBarScroll + remToPixel}px, 0, 0)`}];
      const myAnimationTiming = {duration: tagBarScroll * 30, iterations: Infinity};
      tagBar.animate(myAnimation, myAnimationTiming);
    }
  }
};

const clearTagBarAnimation = function () {
  for (let i = 0; i < tagBars.length; i++) {
    const tagBar = tagBars[i];
    const animations = tagBar.getAnimations();
    if (animations.length) {
      const hiddenTags = tagBar.getElementsByClassName('hidden-tag');
      for (let i = 0; i < hiddenTags.length; i++) {
        // Source of the extra 10px is pagination of tag elements.
        hiddenTags[i].classList.add('hidden');
      }
      for (let i = 0; i < animations.length; i++) {
        animations[i].cancel();
      }
    }
  }
  prepareTagBarAnimation();
};

let timeout;
const delayedTBAnimationRefresh = function () {
  window.clearTimeout(timeout);
  timeout = window.setTimeout(clearTagBarAnimation, 250);
};



window.addEventListener('load', prepareTagBarAnimation);
window.addEventListener('resize', delayedTBAnimationRefresh);
