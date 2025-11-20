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

    // 🔹 List all collections you want to fetch
    const collections = ["anurag718", "anuragrajaryan718", "workrajaryan"];

    // 🔹 Fetch data from each collection and sort records by `sno` to ensure serial (ordered) results
    const results = {};
    for (const col of collections) {
      // sort by sno ascending to preserve serial/order when displayed
      const data = await db.collection(col).find({}).sort({ sno: 1 }).toArray();
      results[col] = data;
    }

    return {
      statusCode: 200,
      body: JSON.stringify(results), // ✅ returns an object with multiple collections
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};
