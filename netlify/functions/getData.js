const { MongoClient } = require("mongodb");

let client = null;

async function getClient() {
  if (!client) {
    client = new MongoClient(process.env.MONGODB_URI);
    await client.connect();
  }
  return client;
}

exports.handler = async function(event, context) {
  try {
    const client = await getClient();
    const db = client.db("code");
    const collection = db.collection("anurag718");

    const data = await collection.find({}).limit(10).toArray();

    return {
      statusCode: 200,
      body: JSON.stringify(data),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};
