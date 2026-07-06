# Response Maps: Returning Data from Responses > Response Map editor: Table Map page > Key > 第1段

When you check the Key option and provide a Sample Key Value, iTest uses the value in the column to find particular rows in the table.

Check the Key checkbox and provide a Sample Key Value to use the value of the token as the key to identify the instance of a repeating block in the response that contains the value that you want to extract. iTest uses the Key token to auto-generate aliases for the other tokens in the block.

In this example, we defined PathCost as a key token:

1. 1 The PathCost token is the Key. Whenever a PathCost value exceeds 25, then the RoleByPathCost query returns the value in that row for the Role token.

![](images/response_mapping.8.jpg) <!-- image_ref -->

1. 2 The PathCost token in this row exceeds 25, so the RoleByPathCost query returns the value in this row for the Role token: TRI.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

If you select UseDefaultValue, then specify a Default value. If you select Error option, only the Step issues view and Error log view are affected and indicates an error (the Query view displays a blank).

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Click Add. The label Indefinite Key appears in the Query column Click Indefinite Key and the Select key column lists the current keys (column names). Click on the required key in the Select key column and it appears in the Query column.

![*](bullet_black_small.png) <!-- image_ref -->

Click on another key in the Select key column to create a compound/combined key Note You may add multiple keys, delete, or move the keys up/down as required.
