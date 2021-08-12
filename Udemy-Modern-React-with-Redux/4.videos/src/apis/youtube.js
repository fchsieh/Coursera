import axios from "axios";

const KEY = 'AIzaSyAK2drGf6SraIczAMYSvPpFoajcK7TQubE';

export default axios.create({
    baseURL: "https://www.googleapis.com/youtube/v3",
    params: {
        part: "snippet",
        maxResults: 5,
        type: 'video',
        key: KEY
    }
});