import axios from 'axios';

export default axios.create({
    baseURL: "https://api.unsplash.com",
    headers: {
        Authorization: "Client-ID D0PIL1AdbLWRYOKqc7yvs5RFQzva5NvZR97g_FBq70w",
    }
});
