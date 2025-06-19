from firebase_functions import https_fn
from firebase_admin import initialize_app, firestore

initialize_app()

@https_fn.on_request()
def py_create_docs(req: https_fn.Request) -> https_fn.Response:
    db = firestore.client()
    i = 1
    while i <= 1:
        doc_num = str(i).rjust(3, "0")
        doc_id = f"doc-{doc_num}"
        print(f"creating doc {doc_id}")
        data = {"name": doc_id, "number": i}
        db.collection("python_collection").document().set(data)
        i+=1
    return https_fn.Response("Created docs!")

@https_fn.on_request()
def py_get_docs(req: https_fn.Request) -> https_fn.Response:
    db = firestore.client()
    docs = db.collection("python_collection").stream()
    i = 0
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
        i+=1
    print(f"total docs: {i}")
    return https_fn.Response(f"total docs: {i}")


@https_fn.on_request()
def py_test(req: https_fn.Request) -> https_fn.Response:
    print("PRINT_STATEMENT - SHOULD ONLY APPEAR ONCE!!!")
    return https_fn.Response("Hello world!")