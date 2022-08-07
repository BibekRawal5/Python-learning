fname = input("Enter the file name: ").strip().lower()


if fname.endswith(".png"):
    print("image/png")
elif fname.endswith(".pdf"):
    print("application/pdf")
elif fname.endswith(".gif"):
    print("image/gif")
elif fname.endswith(".jpg") or fname.endswith(".jpeg"):
    print("image/jpeg")
else:
    print("application/octet-stream")
