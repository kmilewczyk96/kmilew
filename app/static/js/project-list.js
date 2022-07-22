'use strict';

const checkIfFits = function () {
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

window.addEventListener('load', checkIfFits);
window.addEventListener('resize', checkIfFits);

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
