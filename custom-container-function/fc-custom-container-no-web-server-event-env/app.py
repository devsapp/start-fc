import os

if __name__ == '__main__':
    print("Fetch FC event through environment variable 'FC_CUSTOM_CONTAINER_EVENT'")
    print(os.getenv("FC_CUSTOM_CONTAINER_EVENT"))
