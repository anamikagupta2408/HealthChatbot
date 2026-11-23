import faiss
import numpy as np

# Step 1: Create sample vectors
vectors = np.array([
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.8, 0.9, 1.0]
], dtype="float32")

# Step 2: Get vector dimensions
dimension = vectors.shape[1]

# Step 3: Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Step 4: Store vectors in FAISS
index.add(vectors)

# Step 5: Create a query vector
query = np.array([
    [0.1, 0.2, 0.4]
], dtype="float32")

# Step 6: Search for the closest vector
distances, indices = index.search(query, k=2)

# Step 7: Display results
print("Total vectors stored:", index.ntotal)

print("\nClosest vector positions:")
print(indices)

print("\nDistances:")
print(distances)