# Analysis Rules: Validating Responses > When to use a Global rule > Precedence of Global Analysis rules

Global analysis rules are applied in a strictly controlled order. The first rules to be applied are the standard analysis rules associated with the executable step. Thereafter, Global analysis rules are applied in the following order:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Current procedure's analysis rules

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Currently executing test case's analysis rules

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Current procedure's test case's analysis rules (for foreign procedures)

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Current session profile's analysis rules
