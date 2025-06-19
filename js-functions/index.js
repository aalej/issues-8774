const { onRequest } = require("firebase-functions/v2/https");
const { initializeApp } = require("firebase-admin/app")
const { getFirestore } = require("firebase-admin/firestore")
const logger = require("firebase-functions/logger");

// Create and deploy your first functions
// https://firebase.google.com/docs/functions/get-started

initializeApp()
const db = getFirestore()

exports.jsCreateDocs = onRequest((request, response) => {
    for (let i = 1; i <= 1; i++) {
        const docName = `doc-id-${i.toString().padStart(3, "0")}`
        db.collection("js_collection").doc().set({
            name: docName,
            number: i
        })
    }
    response.send("Created docs!");
});

exports.jsGetDocs = onRequest(async (request, response) => {
    const docSnapshots = await db.collection("collection_name").get()
    console.log(docSnapshots.size)
    response.send(`Document Size: ${docSnapshots.size}`);
});

exports.jsTest = onRequest(async (request, response) => {
    console.log("PRINT_STATEMENT - SHOULD ONLY APPEAR ONCE!!!")
    response.send(`Hello world!`);
});
