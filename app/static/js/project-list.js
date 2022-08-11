'use strict';

const paginatorTop = document.getElementsByClassName('paginator--top')[0];
const projectListGrid = document.getElementsByClassName('project-list-grid')[0];
const tagFilterForm = document.getElementsByClassName('tag-filter-form')[0];
const paginatorLinks = document.getElementsByClassName('paginator-link');
const paginatorBottom = document.getElementsByClassName('paginator--bottom')[0];
const toggleNavBtn = document.getElementsByClassName('btn--collapse')[0];
const filterContainer = document.getElementsByClassName('filter-container')[0];
const filterForm = document.getElementsByClassName('tag-filter-form')[0];

const paginatorBottomVisibility = function () {
  const remToPixel = parseFloat(getComputedStyle(document.documentElement).fontSize);
  const projectListHeight = (remToPixel * 11.2) + paginatorTop.scrollHeight + projectListGrid.scrollHeight;
  const viewportHeight = window.innerHeight;

  if (projectListHeight >= viewportHeight) {
    paginatorBottom.classList.remove('hidden');
  } else {
    paginatorBottom.classList.add('hidden');
  }
};

const toggleFilter = function () {
  filterContainer.classList.toggle('slide-in');
};

const filterStickyFlex = function () {
  const remToPixel = parseFloat(getComputedStyle(document.documentElement).fontSize);
  const filterHeight = (remToPixel * 9.6) + filterForm.scrollHeight;
  const changeToFlex = filterHeight >= window.innerHeight;
  if (changeToFlex) {
    filterForm.classList.remove('sticky');
  } else {
    filterForm.classList.add('sticky');
  }
};

// Prevent from wiping filters during page change:
if (tagFilterForm) {
  for (let i = 0; i < paginatorLinks.length; i++) {
    paginatorLinks[i].addEventListener('click', function (e) {
      e.preventDefault()
      const pageNumber = this.dataset.page
      tagFilterForm.innerHTML += `<input value="${pageNumber}" name="page" hidden>`
      tagFilterForm.submit()
    });
  }
}


window.addEventListener('load', paginatorBottomVisibility);
window.addEventListener('load', filterStickyFlex);
window.addEventListener('resize', paginatorBottomVisibility);
window.addEventListener('resize', filterStickyFlex);
toggleNavBtn.addEventListener('click', toggleFilter);


