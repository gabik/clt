clt
===

Gabi server

- new account - errors in Json array ??
- Check all account JSON returns for Json arrays
- change all request.POST readings in view to:
    if 'price_id' in request.POST:
      price_id = request.POST['price_id']
    else:
      return HttpResponse(json_dump)

