<h1>TP1</h1>
<h2>Partie 2.2</h2>
1. db.getName()<br>
2. db.getCollectionName() <br>
3. db.createUser({user: "MyTest",pwd: passwordPrompt(), roles:[{ role: "readWrite", db:"test"}]})<br>
4. MongoServerError[Location51003]: User "MyTest@test" already exists
<br>
<br>
<h2> Partie 2.2.1 </h2>
3. Nous avons une erreur: MongoServerError[Unauthorized]: Command listDatabases requires authentication<br>
4. db.createUser({user:"mongo-admin", pwd: "passw0rd", roles: [{role: "userAdminAnyDatabase",db:"admin"}],})<br>
5. db.adminCommand({listDatabases: 1})<br>
6.4 Afin de créer un utilisateur dans les db airbnb et sales il est nécéssaire de créer my-admin avec les rôle adéquat dans les différentes db.
Il faut également que my-admin ait les roles dans test. Une fois cela fait il faut s'authentifier avec db.auth("my-admin","azerty")

db.createUser({user:"my-admin",roles:[{role: "dbAdmin",db:"sales"},{role:"readWrite",db:"sales"}],pwd:"azerty"})<br>
db.createUser({user:"my-admin",roles:[{role: "dbAdmin",db:"airbnb"},{role:"readWrite",db:"airbnb"}],pwd:"azerty"})

Une fois cela fait on peut exécuter la commande 
db.createUser({user:"my-user1",pwd:"azerty",roles:[{role: "readWrite", db: "airbnb"}, {role: "read", db:"sales"}]})

<h1>TP2</h2>
<h2>Partie 2.2.1 Premier documents vs tous les documents </h2>
2.1 En tapant db.restaurant.findOne(), on obtient le premier document de la collection

{
  _id: ObjectId('6819cf0688776057c120031d'),
  address: {
    building: '1007',
    coord: [
      -73.856077,
      40.848447
    ],
    street: 'Morris Park Ave',
    zipcode: '10462'
  },
  borough: 'Bronx',
  cuisine: 'Bakery',
  grades: [
    {
      date: 2014-03-03T00:00:00.000Z,
      grade: 'A',
      score: 2
    },
    {
      date: 2013-09-11T00:00:00.000Z,
      grade: 'A',
      score: 6
    },
    {
      date: 2013-01-24T00:00:00.000Z,
      grade: 'A',
      score: 10
    },
    {
      date: 2011-11-23T00:00:00.000Z,
      grade: 'A',
      score: 9
    },
    {
      date: 2011-03-10T00:00:00.000Z,
      grade: 'B',
      score: 14
    }
  ],
  name: 'Morris Park Bake Shop',
  restaurant_id: '30075445'
}
<br>
2.2 Nous obtenons la liste des 20 premiers document de la collction restaurant.

{
  _id: ObjectId('6819cf0688776057c120031d'),
  address: {
    building: '1007',
    coord: [
      -73.856077,
      40.848447
    ],
    street: 'Morris Park Ave',
    zipcode: '10462'
  },
  borough: 'Bronx',
  cuisine: 'Bakery',
  grades: [
    {
      date: 2014-03-03T00:00:00.000Z,
      grade: 'A',
      score: 2
    },
    {
      date: 2013-09-11T00:00:00.000Z,
      grade: 'A',
      score: 6
    },
    {
      date: 2013-01-24T00:00:00.000Z,
      grade: 'A',
      score: 10
    },
    {
      date: 2011-11-23T00:00:00.000Z,
      grade: 'A',
      score: 9
    },
    {
      date: 2011-03-10T00:00:00.000Z,
      grade: 'B',
      score: 14
    }
  ],
  name: 'Morris Park Bake Shop',
  restaurant_id: '30075445'
}
<h2>Partie 2.2.2 Restrictions</h2>
3. On va utiliser la commande db.restaurant.findOne({borough:"Brooklyn"}) pour afficher un document de la collection
{
  _id: ObjectId('6819cf0688776057c120031e'),
  address: {
    building: '469',
    coord: [
      -73.961704,
      40.662942
    ],
    street: 'Flatbush Avenue',
    zipcode: '11225'
  },
  borough: 'Brooklyn',
  cuisine: 'Hamburgers',
  grades: [
    {
      date: 2014-12-30T00:00:00.000Z,
      grade: 'A',
      score: 8
    },
    {
      date: 2014-07-01T00:00:00.000Z,
      grade: 'B',
      score: 23
    },
    {
      date: 2013-04-30T00:00:00.000Z,
      grade: 'A',
      score: 12
    },
    {
      date: 2012-05-08T00:00:00.000Z,
      grade: 'A',
      score: 12
    }
  ],
  name: "Wendy'S",
  restaurant_id: '30112340'
}

4. Pour trouver un restaurant dans brooklyn qui propose de la cuisine française on peut faire cette commande db.restaurant.findOne({borough:"Brooklyn",cuisine:"French"})

{
  _id: ObjectId('6819cf0788776057c1200fbd'),
  address: {
    building: '128',
    coord: [
      -73.9902836,
      40.6873687
    ],
    street: 'Smith Street',
    zipcode: '11201'
  },
  borough: 'Brooklyn',
  cuisine: 'French',
  grades: [
    {
      date: 2014-03-06T00:00:00.000Z,
      grade: 'A',
      score: 10
    },
    {
      date: 2013-03-05T00:00:00.000Z,
      grade: 'A',
      score: 12
    },
    {
      date: 2012-05-17T00:00:00.000Z,
      grade: 'A',
      score: 13
    },
    {
      date: 2011-11-09T00:00:00.000Z,
      grade: 'B',
      score: 17
    }
  ],
  name: 'Bar Tabac',
  restaurant_id: '40808118'
}

5.Pour trouver un restaurant qui a un score de 0 on fait la commande db.restaurant.findOne({"grades.score":0})

{
  _id: ObjectId('6819cf0688776057c120032a'),
  address: {
    building: '1',
    coord: [
      -73.96926909999999,
      40.7685235
    ],
    street: 'East   66 Street',
    zipcode: '10065'
  },
  borough: 'Manhattan',
  cuisine: 'American ',
  grades: [
    {
      date: 2014-05-07T00:00:00.000Z,
      grade: 'A',
      score: 3
    },
    {
      date: 2013-05-03T00:00:00.000Z,
      grade: 'A',
      score: 4
    },
    {
      date: 2012-04-30T00:00:00.000Z,
      grade: 'A',
      score: 6
    },
    {
      date: 2011-12-27T00:00:00.000Z,
      grade: 'A',
      score: 0
    }
  ],
  name: '1 East 66Th Street Kitchen',
  restaurant_id: '40359480'
}

<h2>Partie 2.3 Au boulot !</h2>

1. Si on fait la commande db.restaurant.distinct("cuisine"), on obtient:
[
  'Afghan',
  'African',
  'American ',
  'Armenian',
  'Asian',
  'Australian',
  'Bagels/Pretzels',
  'Bakery',
  'Bangladeshi',
  'Barbecue',
  'Bottled beverages, including water, sodas, juices, etc.',
  'Brazilian',
  'CafÃ©/Coffee/Tea',
  'Café/Coffee/Tea',
  'Cajun',
  'Californian',
  'Caribbean',
  'Chicken',
  'Chilean',
  'Chinese',
  'Chinese/Cuban',
  'Chinese/Japanese',
  'Continental',
  'Creole',
  'Creole/Cajun',
  'Czech',
  'Delicatessen',
  'Donuts',
  'Eastern European',
  'Egyptian',
  'English',
  'Ethiopian',
  'Filipino',
  'French',
  'Fruits/Vegetables',
  'German',
  'Greek',
  'Hamburgers',
  'Hawaiian',
  'Hotdogs',
  'Hotdogs/Pretzels',
  'Ice Cream, Gelato, Yogurt, Ices',
  'Indian',
  'Indonesian',
  'Iranian',
  'Irish',
  'Italian',
  'Japanese',
  'Jewish/Kosher',
  'Juice, Smoothies, Fruit Salads',
  'Korean',
  'Latin (Cuban, Dominican, Puerto Rican, South & Central American)',
  'Mediterranean',
  'Mexican',
  'Middle Eastern',
  'Moroccan',
  'Not Listed/Not Applicable',
  'Nuts/Confectionary',
  'Other',
  'Pakistani',
  'Pancakes/Waffles',
  'Peruvian',
  'Pizza',
  'Pizza/Italian',
  'Polish',
  'Polynesian',
  'Portuguese',
  'Russian',
  'Salads',
  'Sandwiches',
  'Sandwiches/Salads/Mixed Buffet',
  'Scandinavian',
  'Seafood',
  'Soul Food',
  'Soups',
  'Soups & Sandwiches',
  'Southwestern',
  'Spanish',
  'Steak',
  'Tapas',
  'Tex-Mex',
  'Thai',
  'Turkish',
  'Vegetarian',
  'Vietnamese/Cambodian/Malaysia'
]

2. Si on fait la commande db.restaurant.distinct("grades.grade"), on obtient les différentes notes :

[ 'A', 'B', 'C', 'Not Yet Graded', 'P', 'Z' ]

3. Pour obtenir le nombre de restaurant propsant de la cuisine française on fait db.restaurant.countDocuments({cuisine: "French"}), on obtient: 
344

4. Pour obenir le nombre de restaurant situé a Central Avenue on fait: db.restaurant.countDocuments({"address.street":"Central Avenue"}), ce qui nous donne: 10 restaurants

5. db.restaurant.countDocuments({"grades.score":{$gt : 50}}) il y a 349 restaurant au dessus de 50

6. Pour obetnir les restaurants en n'affichant que le nom, l'immeuble et la rue on fait db.restaurant.find({}, { name: 1, "address.building": 1, "address.street": 1, _id: 0 }) on obitent alors tous les restaurants formaté comme ceci 

{
  address: {
    building: '1007',
    street: '1'
  },
  name: 'Morris Park Bake Shop'
}

7. Pour obtenir tous les Burger King et leur quartier on fait db.restaurant.find({}, { name: "Burger King", borough : 1, _id: 0 }), on obtient donc une liste formaté comme ceci
{
  borough: 'Bronx',
  name: 'Burger King'
}

8. Pour trouver les restaurants situé entre Union Street et Union Square on fait db.restaurant.find({ "address.street": { $in: ["Union Street", "Union Square"] } }) 
<br>on obtient 
{
  _id: ObjectId('6819cf0688776057c1200432'),
  address: {
    building: '151',
    coord: [
      -74.00184349999999,
      40.684236
    ],
    street: 'Union Street',
    zipcode: '11231'
  },
  borough: 'Brooklyn',
  cuisine: 'Italian',
  grades: [
    {
      date: 2014-05-03T00:00:00.000Z,
      grade: 'A',
      score: 13
    },
    {
      date: 2013-04-23T00:00:00.000Z,
      grade: 'A',
      score: 12
    },
    {
      date: 2012-02-27T00:00:00.000Z,
      grade: 'A',
      score: 2
    }
  ],
  name: "Ferdinando'S Restaurant",
  restaurant_id: '40369716'
}


9. db.restaurant.find({ "address.coord.1": { $gt: 40.90 } }, { name: 1, "address.coord": 1, _id: 0 })
10. db.restaurant.find({"grades.score": 0, "grades.grade": "A"},{name:1,"grades.score":1,"grades.grade":1, _id:0})

<h2>Partie 2.3.1 Pour les plus balèzes </h2>

1. db.restaurant.find({"address.street": "$regex":"Union"}, {name:1, "address.street":1 ,_id:0})
{
  address: {
    street: 'Unionport Road'
  },
  name: 'Venice Pizza'
}
{
  address: {
    street: 'Union Turnpike'
  },
  name: "P.J.' S"
}

2.db.restaurant.find({ "grades.date": ISODate("2014-02-01T00:00:00Z") },{ name: 1, "grades.date": 1, _id: 0 })

{
  grades: [
    {
      date: 2014-02-01T00:00:00.000Z
    },
    {
      date: 2013-01-10T00:00:00.000Z
    },
    {
      date: 2011-12-22T00:00:00.000Z
    }
  ],
  name: 'Shake Shack'
}
{
    
  grades: [
    {
      date: 2014-08-25T00:00:00.000Z
    },
    {
      date: 2014-02-01T00:00:00.000Z
    },
    {
      date: 2012-12-28T00:00:00.000Z
    },
    {
      date: 2012-07-12T00:00:00.000Z
    },
    {
      date: 2011-12-05T00:00:00.000Z
    }
  ],
  name: 'New Flushing Bakery'
}

<h2>Partie 2.4.1 Premiers pas</h2>

1. la commande nécessite une authentification et la base de données est test et pas tp-mongo la commande: mongoimport   --host localhost   --db test   --collection myUsers   --username "my-admin"   --password "azerty"   --authenticationDatabase test   --file sample_data/users.json

2. use test<br>show collections<br>users
3. db.users.countDocuments()<br>6998


<h2>2. 4. 2.  Créer un élément</h2>

4. db.users.insertOne({nom: "Chuck Norris", age: 77, hobbies: ["Karate", "Kung-fu", "Ruling the world"]});

5. db.users.find({nom: "Chuck Norris"})
[
  {
    _id: ObjectId('681b744270e62bd50cd861e0'),
    nom: 'Chuck Norris',
    age: 77,
    hobbies: [ 'Karate', 'Kung-fu', 'Ruling the world' ]
  }
]

6. db.users.find({nom: "Chuck Norris"},{_id:0})
[
  {
    nom: 'Chuck Norris',
    age: 77,
    hobbies: [ 'Karate', 'Kung-fu', 'Ruling the world' ]
  }
]

7. db.users.find({age:{$gte: 20, $lte: 25}},{name:1,age:1,_id:0})
[
  { age: 23, name: 'Phillips Blake' },
  { age: 20, name: 'Atkins Maxwell' },
  { age: 24, name: 'Vanessa Salas' },
  { age: 22, name: 'Peggy Snider' },
  { age: 24, name: 'Jannie Frazier' },
  { age: 25, name: 'Maribel Burns' },
  { age: 23, name: 'Ross Sanders' },
  { age: 20, name: 'Shauna Wall' },
  { age: 22, name: 'Sweet Robinson' },
  { age: 22, name: 'Gloria Ford' },
  { age: 25, name: 'Karen Glenn' },
  { age: 24, name: 'Jeanine Whitehead' },
  { age: 25, name: 'Alicia Mcguire' },
  { age: 23, name: 'Oliver Pugh' },
  { age: 23, name: 'Johns Briggs' },
  { age: 20, name: 'Patrice Mann' },
  { age: 24, name: 'Holly Bates' },
  { age: 20, name: 'Hillary Warner' },
  { age: 21, name: 'Tasha Hale' },
  { age: 24, name: 'Brooks Huffman' }
]

8. db.users.find({age:{$gte: 30, $lte: 40},gender:"male"},{name:1,age:1,_id:0})
[
  { age: 37, name: 'Hebert Sherman' },
  { age: 33, name: 'Cameron Cline' },
  { age: 37, name: 'Quinn Lott' },
  { age: 34, name: 'Lynn Prince' },
  { age: 39, name: 'Dudley Stokes' },
  { age: 36, name: 'Turner Patton' },
  { age: 30, name: 'Higgins Battle' },
  { age: 40, name: 'Strickland Schmidt' },
  { age: 40, name: 'Bruce Mclaughlin' },
  { age: 37, name: 'Zimmerman Kent' },
  { age: 35, name: 'Barber Hewitt' },
  { age: 37, name: 'Osborne Levine' },
  { age: 39, name: 'Morton Hoffman' },
  { age: 33, name: 'Rodgers Langley' },
  { age: 34, name: 'Wilson Owens' },
  { age: 32, name: 'Macdonald Holmes' },
  { age: 31, name: 'Simon Adams' },
  { age: 38, name: 'Randolph York' },
  { age: 33, name: 'Vang Bryan' },
  { age: 32, name: 'Wilcox Peterson' }
]


9. db.users.find({},{name:1,_id:0,state:"Louisiana"}).
[
  { name: 'Lynette Mercer', state: 'Louisiana' },
  { name: 'Corine Mccormick', state: 'Louisiana' },
  { name: 'Morgan Sosa', state: 'Louisiana' },
  { name: 'Stacie Rivera', state: 'Louisiana' },
  { name: 'Phillips Blake', state: 'Louisiana' },
  { name: 'Charlotte Jefferson', state: 'Louisiana' },
  { name: 'Mcmahon Jimenez', state: 'Louisiana' },
  { name: 'Jeannine Haney', state: 'Louisiana' },
  { name: 'Heidi Lancaster', state: 'Louisiana' },
  { name: 'Wheeler Boyer', state: 'Louisiana' },
  { name: 'Mcpherson Harrington', state: 'Louisiana' },
  { name: 'Myrtle Becker', state: 'Louisiana' },
  { name: 'Atkins Maxwell', state: 'Louisiana' },
  { name: 'Lana Pruitt', state: 'Louisiana' },
  { name: 'Hebert Sherman', state: 'Louisiana' },
  { name: 'Cameron Cline', state: 'Louisiana' },
  { name: 'Casey Gill', state: 'Louisiana' },
  { name: 'Frost Franks', state: 'Louisiana' },
  { name: 'Cara Young', state: 'Louisiana' },
  { name: 'Ida Coffey', state: 'Louisiana' }
]

10. Si on affiche que l'age le nom et l'email par exemple on fait :<br>db.users.find({},{name:1,email:1,_id:0,age:1}).sort({ age: -1 }).limit(20)<br><br>ça nous évite d'afficher toutes les informations.<br>Sinon on peut faire  db.users.find().sort({ age: -1 }).limit(20) si on veut le détails des utilisateurs<br>Voici le réultat avec la commande qui nous affiche l'age, le nom, et l'email.
[
  { age: 77, name: 'Chuck Norris' },
  {
    age: 60,
    name: 'Chrystal Booth',
    email: 'chrystalbooth@retrack.com'
  },
  {
    age: 60,
    name: 'Dollie Espinoza',
    email: 'dollieespinoza@retrack.com'
  },
  { age: 60, name: 'Hardin Conrad', email: 'hardinconrad@retrack.com' },
  { age: 60, name: 'Delia Stark', email: 'deliastark@retrack.com' },
  { age: 60, name: 'Daphne Larson', email: 'daphnelarson@retrack.com' },
  {
    age: 60,
    name: 'Clayton Mullen',
    email: 'claytonmullen@retrack.com'
  },
  { age: 60, name: 'Dianne Velez', email: 'diannevelez@retrack.com' },
  { age: 60, name: 'Bianca Sims', email: 'biancasims@retrack.com' },
  { age: 60, name: 'Myrtle Becker', email: 'myrtlebecker@retrack.com' },
  {
    age: 60,
    name: 'Watson Beasley',
    email: 'watsonbeasley@retrack.com'
  },
  {
    age: 60,
    name: 'Jeannine Haney',
    email: 'jeanninehaney@retrack.com'
  },
  {
    age: 60,
    name: 'Annmarie Brennan',
    email: 'annmariebrennan@retrack.com'
  },
  {
    age: 60,
    name: 'Madelyn Nguyen',
    email: 'madelynnguyen@retrack.com'
  },
  {
    age: 60,
    name: 'Livingston Smith',
    email: 'livingstonsmith@retrack.com'
  },
  {
    age: 60,
    name: 'Sutton Stephenson',
    email: 'suttonstephenson@retrack.com'
  },
  {
    age: 60,
    name: 'Reeves Thompson',
    email: 'reevesthompson@retrack.com'
  },
  { age: 60, name: 'Hull Kidd', email: 'hullkidd@retrack.com' },
  {
    age: 60,
    name: 'Hickman Branch',
    email: 'hickmanbranch@retrack.com'
  },
  { age: 60, name: 'Ruthie Estes', email: 'ruthieestes@retrack.com' }
]


11. La commande pour compter le nombre de femmes agées on fait la commande : db.users.countDocuments({gender:"female",age:30}) <br>on obtient 63 femmes agées de 30 ans 

12. Pour mettre tous les champs a jour on fait:  db.users.updateMany({}, { $unset: { phone: "" } })

13. Pour mettre a jour l'age de Chuck Norris on fait db.users.updateOne({ nom: "Chuck Norris" },{ $set: { age: "infinity" } })

14. $push nous permet de faire un append dans les listes dans mongodb db.users.updateMany({ age: { $gt: 50 } },{ $push: { hobbies: "jardinage" } })

<h2> Partie 2.4.5 Aggrégation</h2>

15. db.users.aggregate([ { $group: { _id: "$address.state", quantity: { $sum: 1 } } }, { $sort: { total: -1 } }] )
[
  { _id: 'Washington', quantity: 142 },
  { _id: 'Missouri', quantity: 143 },
  { _id: 'South Dakota', quantity: 142 },
  { _id: 'North Carolina', quantity: 143 },
  { _id: 'Maryland', quantity: 143 },
  { _id: 'Wisconsin', quantity: 143 },
  { _id: 'Massachusetts', quantity: 143 },
  { _id: 'Georgia', quantity: 143 },
  { _id: 'Pennsylvania', quantity: 143 },
  { _id: 'Nebraska', quantity: 143 },
  { _id: 'Kentucky', quantity: 143 },
  { _id: 'Arizona', quantity: 142 },
  { _id: 'Michigan', quantity: 143 },
  { _id: 'South Carolina', quantity: 142 },
  { _id: 'Alabama', quantity: 143 },
  { _id: 'New Hampshire', quantity: 143 },
  { _id: 'Idaho', quantity: 143 },
  { _id: 'Connecticut', quantity: 143 },
  { _id: 'Oregon', quantity: 143 },
  { _id: 'New York', quantity: 142 }
]

16. db.users.aggregate([{ $group: { _id: "$address.state", averageAge: { $avg: "$age" } } }, { $sort: { _id: 1 } }])

[
  { _id: null, averageAge: 77 },
  { _id: 'Alabama', averageAge: 36.88811188811189 },
  { _id: 'Alaska', averageAge: 34.86013986013986 },
  { _id: 'Arizona', averageAge: 35.056338028169016 },
  { _id: 'Arkansas', averageAge: 36.72727272727273 },
  { _id: 'California', averageAge: 35.60839160839161 },
  { _id: 'Colorado', averageAge: 35.93006993006993 },
  { _id: 'Connecticut', averageAge: 33.35664335664335 },
  { _id: 'Delaware', averageAge: 34.3986013986014 },
  { _id: 'Florida', averageAge: 35.38461538461539 },
  { _id: 'Georgia', averageAge: 34.73426573426573 },
  { _id: 'Hawaii', averageAge: 38.16901408450704 },
  { _id: 'Idaho', averageAge: 35.25874125874126 },
  { _id: 'Illinois', averageAge: 33.49650349650349 },
  { _id: 'Indiana', averageAge: 35.95804195804196 },
  { _id: 'Iowa', averageAge: 36.267605633802816 },
  { _id: 'Kansas', averageAge: 33.72727272727273 },
  { _id: 'Kentucky', averageAge: 33.75524475524475 },
  { _id: 'Louisiana', averageAge: 33.51048951048951 },
  { _id: 'Maine', averageAge: 35.0979020979021}

]

17. db.users.aggregate([{ $unwind: "$hobbies" },{ $group: { _id: "$address.city", hobbies: { $addToSet: "$hobbies" } } },{ $sort: { _id: 1 } }])
[
  {
    _id: null,
    hobbies: [ 'Karate', 'Ruling the world', 'Kung-fu', 'jardinage' ]
  },
  {
    _id: 'Aberdeen',
    hobbies: [
      'poney',
      'cooking',
      'computer science',
      'swimming',
      'kung-fu',
      'running',
      'jardinage',
      'gaming',
      'cinema',
      'reading'
    ]
  },
  {
    _id: 'Abiquiu',
    hobbies: [
      'cooking', 'swimming',
      'kung-fu', 'running',
      'music',   'jardinage',
      'theatre', 'cinema',
      'gaming',  'reading'
    ]
  },
  {
    _id: 'Abrams',
    hobbies: [
      'poney',
      'cooking',
      'computer science',
      'swimming',
      'kung-fu',
      'running',
      'jardinage',
      'cinema',
      'gaming'
    ]
  },
  {
    _id: 'Accoville',
    hobbies: [
      'swimming', 'theatre',
      'gaming',   'music',
      'kung-fu',  'cinema',
      'running',  'cooking',
      'reading',  'jardinage'
    ]
  },
  {
    _id: 'Ada',
    hobbies: [
      'running',
      'music',
      'jardinage',
      'gaming',
      'theatre',
      'cinema',
      'poney',
      'computer science'
    ]
  },
  {
    _id: 'Adamstown',
    hobbies: [
      'cinema',
      'swimming',
      'running',
      'kung-fu',
      'computer science',
      'cooking',
      'reading',
      'gaming'
    ]
  },
  {
    _id: 'Adelino',
    hobbies: [
      'jardinage',
      'computer science',
      'music',
      'gaming',
      'cinema',
      'reading',
      'cooking',
      'running',
      'swimming'
    ]
  },
  {
    _id: 'Advance',
    hobbies: [
      'cinema',
      'swimming',
      'jardinage',
      'cooking',
      'running',
      'computer science',
      'reading'
    ]
  },
  {
    _id: 'Aguila',
    hobbies: [
      'jardinage',
      'theatre',
      'poney',
      'running',
      'kung-fu',
      'music',
      'computer science'
    ]
  },
  {
    _id: 'Ahwahnee',
    hobbies: [
      'jardinage',
      'gaming',
      'computer science',
      'running',
      'reading',
      'cooking',
      'poney',
      'music',
      'swimming'
    ]
  },
  {
    _id: 'Alafaya',
    hobbies: [
      'cooking',   'swimming',
      'kung-fu',   'music',
      'jardinage', 'theatre',
      'cinema',    'gaming'
    ]
  },
  {
    _id: 'Alamo',
    hobbies: [
      'theatre', 'swimming',
      'running', 'kung-fu',
      'poney',   'cooking',
      'reading', 'gaming'
    ]
  },
  {
    _id: 'Albany',
    hobbies: [
      'reading',
      'jardinage',
      'gaming',
      'theatre',
      'cinema',
      'running',
      'swimming',
      'computer science',
      'music',
      'cooking',
      'poney'
    ]
  },
  {
    _id: 'Albrightsville',
    hobbies: [
      'kung-fu',   'gaming',
      'jardinage', 'reading',
      'cinema',    'poney',
      'cooking',   'swimming',
      'music'
    ]
  },
  {
    _id: 'Alden',
    hobbies: [
      'poney',
      'cooking',
      'swimming',
      'running',
      'kung-fu',
      'music',
      'computer science',
      'cinema',
      'jardinage',
      'reading'
    ]
  },
  {
    _id: 'Alderpoint',
    hobbies: [
      'jardinage',
      'swimming',
      'computer science',
      'music',
      'kung-fu',
      'running',
      'cooking',
      'gaming',
      'reading',
      'theatre'
    ]
  },
  {
    _id: 'Alfarata',
    hobbies: [
      'jardinage',
      'cinema',
      'music',
      'kung-fu',
      'running',
      'poney',
      'theatre',
      'cooking',
      'computer science',
      'swimming',
      'gaming'
    ]
  },
]

18. db.users.aggregate([{$project: {_id: 0,name: { $toLower: "$name" },age: 1}}])
<br>[
  { age: 59, name: 'lynette mercer' },
  { age: 58, name: 'corine mccormick' },
  { age: 53, name: 'morgan sosa' },
  { age: 30, name: 'stacie rivera' },
  { age: 23, name: 'phillips blake' },
  { age: 39, name: 'charlotte jefferson' },
  { age: 17, name: 'mcmahon jimenez' },
  { age: 60, name: 'jeannine haney' },
  { age: 56, name: 'heidi lancaster' },
  { age: 57, name: 'wheeler boyer' },
  { age: 58, name: 'mcpherson harrington' },
  { age: 60, name: 'myrtle becker' },
  { age: 20, name: 'atkins maxwell' },
  { age: 53, name: 'lana pruitt' },
  { age: 37, name: 'hebert sherman' },
  { age: 33, name: 'cameron cline' },
  { age: 48, name: 'casey gill' },
  { age: 43, name: 'frost franks' },
  { age: 12, name: 'cara young' },
  { age: 49, name: 'ida coffey' }
]

19. db.users.aggregate([{ $match: { gender: "male" } },{ $group: { _id: "$address.state", averageAge: { $avg: "$age" } } },{ $sort: { averageAge: -1 } }]) <br>
[
  { _id: 'Hawaii', averageAge: 38.921052631578945 },
  { _id: 'Colorado', averageAge: 38.357142857142854 },
  { _id: 'Arkansas', averageAge: 37.92307692307692 },
  { _id: 'New Hampshire', averageAge: 37.890625 },
  { _id: 'Nevada', averageAge: 37.58730158730159 },
  { _id: 'Indiana', averageAge: 36.9746835443038 },
  { _id: 'New Mexico', averageAge: 36.63076923076923 },
  { _id: 'Missouri', averageAge: 36.44318181818182 },
  { _id: 'Maryland', averageAge: 36.426829268292686 },
  { _id: 'Pennsylvania', averageAge: 36 },
  { _id: 'Tennessee', averageAge: 35.85333333333333 },
  { _id: 'Virginia', averageAge: 35.73684210526316 },
  { _id: 'Illinois', averageAge: 35.71641791044776 },
  { _id: 'Ohio', averageAge: 35.529411764705884 },
  { _id: 'New York', averageAge: 35.50617283950617 },
  { _id: 'Minnesota', averageAge: 35.33846153846154 },
  { _id: 'Alaska', averageAge: 35.298507462686565 },
  { _id: 'Massachusetts', averageAge: 35.278688524590166 },
  { _id: 'North Carolina', averageAge: 35.27777777777778 },
  { _id: 'Mississippi', averageAge: 35.225352112676056 }
]


<h1>TP3</h1>

<h2>1. Introduction</h2>

1. B.Établir des connexions sécurisées avec un cluster MongoDB et exécuter des opérations de base de données
pour le compte d’applications clientes

2. B.PyMongo