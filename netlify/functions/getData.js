

const { MongoClient } = require("mongodb");

let client = null;

async function getClient() {
  if (!client) {
    client = new MongoClient(process.env.MONGODB_URI);
    await client.connect();
  }
  return client;
}

exports.handler = async function (event, context) {
  try {
    const client = await getClient();
    const db = client.db("code");
    const collection = db.collection("anurag718");

    const result = await collection.find({}).toArray();

    return {
      statusCode: 200,
      body: JSON.stringify(result),  // ✅ use result, not undefined data
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};


