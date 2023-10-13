import { getCookie } from "./utils.js"

const BASE_URL = 'http://localhost:8000/'
const FETCH_HEADERS = {
  "X-CSRFToken": getCookie('csrftoken'),
}



export { BASE_URL, FETCH_HEADERS }