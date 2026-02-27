


async def new_order_handler(data):


async def get_products(client, last_id):
  url = mpfit + ""
  body = {
  "limit": 200,
  "last_id": last_id
  }
  result = await client.post(url=url, headers=mpfit_headers, json=body)
  result = result.json()
  #products = result["data"]
  if len(result["data"]) == 200:
    products = await get_products(client, result["last_id"])
    products.extend(result["data"])
  return products
