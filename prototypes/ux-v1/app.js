const views=[...document.querySelectorAll('.view')];
const navButtons=[...document.querySelectorAll('nav [data-view]')];
for(const button of navButtons){button.addEventListener('click',()=>{const id=button.dataset.view;for(const view of views)view.hidden=view.id!==id;for(const candidate of navButtons){if(candidate===button)candidate.setAttribute('aria-current','page');else candidate.removeAttribute('aria-current')}document.getElementById(id).querySelector('h1')?.focus?.();document.getElementById('main').focus()})}
const dialog=document.getElementById('audit-dialog');
document.querySelector('[data-open-dialog]')?.addEventListener('click',()=>dialog.showModal());
document.querySelector('[data-close-dialog]')?.addEventListener('click',()=>dialog.close());
dialog?.addEventListener('cancel',()=>dialog.close());
