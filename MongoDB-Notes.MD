## MongoDB Notes

1. How to Import Data from Another File
   1. mongodb import <> filename


- MongoDB Tools: The video highlights several MongoDB tools, including mongostat, mongodump, mongorestore, mongoexport, and mongoimport.
- Using mongoimport: The primary focus is on using the mongoimport command to import data from JSON or CSV files into MongoDB.
- Import Process: The process involves specifying the username, authentication database, target database, and the file to be imported. The example imports three datasets (inventory.json, movies.json, and orders.json) into the sample_data database.
- Check Log Files: If your MongoDB deployment fails to start, check the log files for errors.
- Disable Fork Option: If the deployment isn't starting, try disabling the fork option in the configuration file to see the error directly.
- Check the Oplog: Use the db.oplog.rs.find command to check the oplog for issues.
Increase Log Level: Adjust the log level to get more detailed information for debugging.
- Community Support: Utilize resources like Stack Overflow to find solutions from the community.


MongoDB Formats:

1. JSON Documents: MongoDB is built to work natively with JSON documents, allowing you to store data as is.
2. Key-Value Pairs: JSON documents consist of key-value pairs, where keys are strings and values can be strings, numbers, booleans, arrays, or other JSON objects.
3. BSON: MongoDB uses BSON (binary encoded serialization of JSON-like documents) for storage, which is lightweight and efficient, supporting additional types like images and timestamps.


`Mongodb Deployment`

1. Database Deployment: MongoDB deployment can contain multiple databases, each organized into collections.
2. Collections: Collections are groupings of MongoDB documents, such as a user's collection or a posts collection.
3. Documents: Documents are the basic units of data in MongoDB, each containing an individual record. Each document must have a unique ID, which MongoDB can generate automatically.


`"MongoDB Query Language"`

1. CRUD Operations: The MongoDB query language (MQL) allows you to perform Create, Read, Update, and Delete operations on your data.
2. Insert Commands: Use insertOne to add a single document and insertMany to add multiple documents.
3. Read Commands: Use findOne to retrieve a single document and find to retrieve multiple documents, with optional conditions to filter results.
4. Update Commands: Use updateOne to update a single document and updateMany to update multiple documents, using the $set operator to specify changes.
5. Delete Commands: Use deleteOne to remove a single document and deleteMany to remove multiple documents based on specified conditions.

`"Indexes" video:`

1. Purpose of Indexes: Indexes in MongoDB help speed up query execution by allowing the database to quickly locate the data without scanning the entire collection.
2. Types of Indexes: There are various types of indexes, including single field, compound, multi-key, text, wildcard, and geometric indexes, each serving different query needs.
3. Trade-offs: While indexes improve read performance, they add about 10% overhead to write operations. It's important to create indexes based on common query patterns to balance performance.

`Types of Indexes`

1. Single Field Indexes: These create an index on just one field, making queries on that field faster.
2. Compound Indexes: These create an index on a combination of fields, useful for queries that often involve multiple fields together.
3. Multi-key Indexes: These are used for indexing array values. They can index up to one array value per document.
4. Text Indexes: These allow you to search within text fields, useful for full-text search queries.
5. Wildcard Indexes: These are special indexes that can index fields with dynamic schema, useful for very diverse data.
6. Geometric Indexes: These include 2D sphere, 2D, and geoHaystack indexes, used for geospatial queries.
7. Hashed Indexes: These reduce the index size for large values but are not suitable for range queries.

Indexes in MongoDB are a powerful tool for improving read performance by allowing the database to quickly locate data. However, they come with 

`trade-offs:`

1. Read Performance: Indexes significantly speed up read operations because the database can quickly find the indexed data without scanning the entire collection.
2. Write Performance: Indexes add overhead to write operations (inserts, updates, deletes) because the database must also update the indexes whenever the indexed fields are modified. This can add about 10% overhead to write operations.
3. Storage Space: Indexes consume additional disk space. Each index you create requires storage, which can be significant depending on the size of your data.
4. Balancing Act: It's crucial to create indexes based on common query patterns. This means analyzing your application's query needs and creating indexes that will most benefit the queries you run most frequently. Over-indexing can lead to unnecessary overhead and storage consumption, while under-indexing can result in slower read performance.

`"insertOne and insertMany"`

1. Insert Commands: Use insertOne to insert a single document and insertMany to insert multiple documents at once.
2. Durability: Ensures that acknowledged writes are permanently stored in the database, even if parts of it become temporarily unavailable. Higher durability means slower writes but safer data.
3. writeConcern: Configures the level of durability. It includes options like w (number of instances that must acknowledge the write), j (whether writes are written to disk or just in-memory), and wtimeout (time limit to prevent writes from blocking indefinitely).


`"findOne and find"`

1. findOne and find Commands: findOne retrieves a single document, while find retrieves multiple documents based on specified criteria.
2. Querying Collections: You can explore collections by switching databases and using commands like show dbs and db.collection.findOne.
3. Nested Queries and Array Values: Learn how to perform nested queries and access specific items in arrays using dot notation (e.g., ratings.mndb and genres.0).
4. Read Concern and Read Preference: Configure read behavior with readConcern to ensure data consistency and availability, and use readPreference to optimize read performance.

Comparison Operators: MongoDB supports several comparison operators, including $eq (equal), $gt (greater than), $gte (greater than or equal), $lt (less than), $lte (less than or equal), and $ne (not equal).

Usage in Queries: These operators are used to filter documents based on specific conditions. For example, finding documents where a field's value is greater than or equal to a certain number.

Special Operators: The video also covers $in (matches any of the values specified in an array) and $nin (matches none of the values specified in an array), which are useful for more complex queries.


$gte (greater than or equal):
javascript
db.inventory.find({ "variations.quantity": { $gte: 8 } })

This query finds documents where the quantity in the variations array is greater than or equal to 8.

$lt (less than):
javascript
db.cars.find({ "price": { $lt: 2000 } })

This query finds documents where the price is less than 2000.

$in (matches any of the values specified in an array):
javascript
db.cars.find({ "variations.variation": { $in: ["blue", "red"] } })

This query finds documents where the variation is either blue or red.

$nin (matches none of the values specified in an array):
javascript
db.cars.find({ "variations.variation": { $nin: ["blue", "red"] } })

This query finds documents where the variation is neither blue nor red.


"Logical operators" video:

Logical Operators: MongoDB supports four logical operators: $and, $or, $nor, and $not.
Usage in Queries: These operators are used to combine multiple conditions in a query. For example, $and requires all conditions to be met, while $or requires at least one condition to be met.
Examples:
$and: Finds documents matching multiple conditions, such as quantity not being zero and the quantity field existing.
$or: Finds documents matching at least one condition, such as cars that are either blue, green, or teal.
$nor: Finds documents that do not match any of the specified conditions, such as cars with a price not greater than 8,000 and not blue.
$not: Used to negate a condition, such as finding cars where the price is not greater than 2,000.


$and:
javascript
db.inventory.find({
$and: [
{ "variations.quantity": { $ne: 0 } },
{ "variations.quantity": { $exists: true } }
]
})

This query finds documents where the quantity is not zero and the quantity field exists.

$or:
javascript
db.inventory.find({
$or: [
{ "variations.variation": "blue" },
{ "variations.variation": "green" },
{ "variations.variation": "teal" }
]
})

This query finds documents where the variation is either blue, green, or teal.

$nor:
javascript
db.inventory.find({
$nor: [
{ "price": { $gt: 8000 } },
{ "variations.variation": "blue" }
]
})

This query finds documents where the price is not greater than 8,000 and the variation is not blue.

$not:
javascript
db.inventory.find({
"price": { $not: { $gt: 2000 } }
})

This query finds documents where the price is not greater than 2,000.