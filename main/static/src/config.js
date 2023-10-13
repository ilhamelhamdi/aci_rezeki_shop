import { getCookie } from "./utils.js"

const BASE_URL = (new URL(window.location.href)).origin
const FETCH_HEADERS = {
  "X-CSRFToken": getCookie('csrftoken'),
}



export { BASE_URL, FETCH_HEADERS }