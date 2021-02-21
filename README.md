# basket

**Api**
- URL
```
http://localhost:8000/api/groceries/items/
or
http://basket-grocery.herokuapp.com/api/groceries/all/
```
- method:- GET
- Retrun the list of GroceryItems register based on parameters.
- Parameter
  - search:- search the list of grocery items on the basis of an input string that finds matches(case insensitive) in title and description
  - parameter:- Allow parameters for sorting by price and creation time.
  - ordering:- ascending or descending

- Location:- https://github.com/Shagunjain10/basket/tree/main/groceries/api

- pagination [Query Params]
  - items:- Number of Items in one page
  - totalpage:- All items divided into total pages
