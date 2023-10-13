import { BASE_URL, FETCH_HEADERS } from './config.js'

const fetchItems = async () => {
  let items = await fetch(`${BASE_URL}/json/`, { headers: FETCH_HEADERS })
  items = await items.json()
  let itemsHTML = ''
  items.forEach(item => {
    itemsHTML += `
    <a href="/item/${item.pk}" class="item-card shadow">
      <img src="${item.fields.image}" class="item-image"></img>
      <div class="item-contents">
        <p class="item-name">${item.fields.name}</p>
        <p class="item-description">${item.fields.description}</p>
        <div class="item-field">
          <span>Price</span>
          <span>Rp${item.fields.price}</span>
        </div>
        <div class="item-field">
          <span>Stock</span>
          <span>${item.fields.amount}</span>
        </div>
      </div>
    </a>
    `
  })
  document.getElementById('item-card-wrapper').innerHTML = itemsHTML
  document.getElementById('item-count').innerHTML = items.length
}

const addItem = async () => {
  const form = document.getElementById('add-item-form')
  let response = await fetch(`${BASE_URL}/create-ajax/`, {
    method: 'POST',
    headers: FETCH_HEADERS,
    body: new FormData(form)
  })
  if (response.status == 201) {
    document.getElementById('add-item-form').reset()
    fetchItems()
    $('#add-item-modal').modal('hide')
  }
}

fetchItems()

document.getElementById('add-item-form').addEventListener('submit', e => {
  e.preventDefault()
  addItem()
})