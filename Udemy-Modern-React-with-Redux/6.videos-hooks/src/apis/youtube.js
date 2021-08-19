import axios from "axios";

const KEY = "AIzaSyDTYpJss41Ly8OyHJAgBC5P8Id0WCV895c";

export default axios.create({
  baseURL: "https://www.googleapis.com/youtube/v3",
  params: {
    part: "snippet",
    maxResults: 5,
    type: "video",
    key: KEY,
  },
});
