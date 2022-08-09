'use strict';


const paginatorBottomVisibility = function () {
  // Add bottom paginator if doc height > viewport height:
  const documentHeight = document.documentElement.scrollHeight;
  const viewportHeight = window.innerHeight;

  console.log(documentHeight, viewportHeight)
  if (documentHeight > viewportHeight) {
    paginatorBottom.classList.remove('hidden');
  } else {
    paginatorBottom.classList.add('hidden');
  }
};

window.addEventListener('load', paginatorBottomVisibility);
window.addEventListener('resize', paginatorBottomVisibility);

const tagFilterForm = document.getElementsByClassName('tag-filter-form')[0];
const paginatorLinks = document.getElementsByClassName('paginator-link');
const paginatorBottom = document.getElementsByClassName('paginator--bottom')[0];

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

const toggleNavBtn = document.getElementsByClassName('btn--collapse')[0];
const filterContainer = document.getElementsByClassName('filter-container')[0];
const toggleFilter = function () {
  filterContainer.classList.toggle('slide-in');
};

toggleNavBtn.addEventListener('click', toggleFilter);


const filterForm = document.getElementsByClassName('tag-filter-form')[0];
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

window.addEventListener('load', filterStickyFlex);
window.addEventListener('resize', filterStickyFlex);


