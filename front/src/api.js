import axios from "axios";
import { getLocalToken } from "./utils/utils";

const ServerHost = process.env.REACT_APP_BACKEND_HOST;

function authHeaders(token) {
  if (!token) {
    token = getLocalToken();
  }

  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async logInGetToken(username, password) {
    // const params = new URLSearchParams();
    // params.append('username', username);
    // params.append('password', password);
    return axios.post(
      `${ServerHost}/login/access-token`,
      `grant_type=&username=${username}&password=${password}`,
      {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          accept: "application/json",
        }
      }
    );
  },
  async getHomeInfo() {
    return axios.get(`${ServerHost}/home`, authHeaders());
  },

  async getMoreList(page) {
    return axios.get(`${ServerHost}/home-list?page_no=${page}`, authHeaders());
  },

  async getDetail(id) {
    return axios.get(`${ServerHost}/article?article_id=${id}`, authHeaders());
  },

  async createArticle(title, content) {
    return axios.post(
      `${ServerHost}/article`,
      {
        title: title,
        desc: title,
        content: content,
        img_url: "img_url",
      },
      authHeaders()
    );
  },
};
