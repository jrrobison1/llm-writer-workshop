# Use a lightweight Node.js base image for your frontend applications
FROM node:18-alpine

# Create the working directory inside the container
WORKDIR /app

# Copy necessary dependencies first for optimized layer caching
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the rest of the project files
COPY . .

# Build the production-ready image of your React app
RUN npm run build

# Expose the port on which the app will run (default is 3000 for React)
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
