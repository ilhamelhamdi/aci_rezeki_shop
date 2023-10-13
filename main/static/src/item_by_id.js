import { BASE_URL, FETCH_HEADERS } from './config.js'

const getItemById = async () => {
  const path = window.location.pathname.split('/')
  const id = path[path.length - 1]
  let item = await fetch(`${BASE_URL}/json/${id}`, { headers: FETCH_HEADERS })
  item = await item.json()
  let itemHTML = `
      <div class="image-wrapper">
        <img src="${item.fields.image}" alt="">
      </div>
      <div class="text-wrapper">
        <h1 class="item-name">${item.fields.name}</h1>
        <span class="item-price">Rp${item.fields.price}</span>
        <div class="item-meta">
          <span>Category: ${item.fields.category}</span>
          <span>Stock: 
            <button class="btn-primary count-btn" id="decrement_stock">-</button>
            <span style="font-weight: bold;">${item.fields.amount}</span>
            <button class="btn-primary count-btn" id="increment_stock">+</button>
          </span>
        </div>
        <div class="item-description">
          <h2>Description</h2>
          <p>${item.fields.description}</p>
        </div>
        <button class="btn btn-danger" onclick="() => {deleteItem(${item.fields.pk})}">Delete</button>
      </div>
    `
  document.getElementById('content-wrapper').innerHTML = itemHTML
}

const deleteItem = (id) => {
  fetch(`${BASE_URL}/delete-item/${id}/`, {
    method: 'DELETE',
    headers: FETCH_HEADERS
  })
  window.location.href = '/'
}