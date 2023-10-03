inc_button = document.getElementById('increment_stock')
dec_button = document.getElementById('deccrement_stock')

inc_button.addEventListener('click', () => {
  fetch('http://localhost:8000/update-item/', {
    method: 'PUT',
    
  })
});