=====SETTINGS=====
The settings are all in the settings app. There are multiple files
within the settings folder which are used in different environments.

=====URLS=====
The URL structure is a general structure for django. Try to not use
the identifier in the URL strings because it looks better when
using a slug. Don't put business logic into the url strings.

=====MODELS=====
Use fat models. Put as much logic on the model as possible. This project 
uses abstract models when possible to reduce the amount of model fields/logic
that needs to be repeated.

=====VIEWS=====
Try to only use Class-Based views in this project. Rarely it will be 
necessary to use Function-Based views, but definitely try to use CBV
first.

=====TEMPLATES=====
This project is using a structure of Templates/(app)content and 
Templates/(app)include. For reusable content (both base files, and
general includes), use the include folder. Each app should have its
own base.html file, which usually inherits from maininclude/base.html,
however it gives the flexibility to change the base file, or header/footer
if needed.