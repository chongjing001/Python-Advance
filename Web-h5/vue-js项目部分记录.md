### Vue.js 扩展部分记录

#### axios封装



```javascript
import axios from "axios";

const Axios = axios.create({
  timeout: 10 * 1000,
  baseURL: '/api',
  withCredentials: true,
});

Axios.interceptors.request.use(
  (config) => {
    // 在发送请求之前做些什么
    if (!config.headers["Authorization"]){
      // .... 
    }
      
    return config;
  },
  (error) => {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

Axios.interceptors.response.use(
  (res) => {
    if (res.data && res.data.code) {

      switch (Number(res.data.code)) {
        case 1001:
          res.data.error_msg = "....";
          break;
        default:
          break;
      }
    }
    return Promise.resolve(res);
  },
  (err) => {
    if (err && err.response) {
      switch (err.response.status) {
        case 400:
          err.message = "错误请求"; // 错误请求
          break;
        case 401:
        case 422:
          err.message = "未授权，请重新登录"; // 未授权，请重新登录
          break;
        case 403:
          err.message = "拒绝访问"; // 拒绝访问
          break;
        case 404:
          err.message = "请求错误,未找到该资源"; // 请求错误,未找到该资源
          break;
        case 405:
          err.message = "请求方法未允许"; // 请求方法未允许
          break;
        case 408:
          err.message = "请求超时"; // 请求超时
          break;
        case 500:
          err.message = "服务器端出错"; // 服务器端出错
          break;
        case 501:
          err.message = "网络未实现"; // 网络未实现
          break;
        case 502:
          err.message = "网络错误"; // 网络错误
          break;
        case 503:
          err.message = "服务不可用"; // 服务不可用
          break;
        case 504:
          err.message = "网络超时"; // 网络超时
          break;
        case 505:
          err.message = "http版本不支持该请求"; // http版本不支持该请求
          break;
        default:
          err.message = `连接错误${err.response.status}`; // 连接错误${err.response.status}
      }
    } else {
      err.message = "连接到服务器失败"; // 连接到服务器失败
    }
    return Promise.reject(err);
  }
);

export default Axios;
```

##### 提示信息和错误信息统一处理

```javascript
import axios from "@/utils/validate";
import { msg_error, msg_success } from "@/utils/message_tip"


async function send_req(url, method='get', body = null, tip_msg="") {

    try {
        method = method.toLowerCase()
        let resp = null
        let default_tip_msg = ""
        switch (method){       
            case 'get':
                resp = await axios.get(url)
                break
            case 'post':
                resp = await axios.post(url, body)
                default_tip_msg = '添加成功'
                break
            case 'put':
                resp = await axios.put(url, body)
                default_tip_msg = '更新成功'
                break
            case 'delete':
                resp = await axios.delete(url)
                default_tip_msg = '删除成功'
            
        }
        if(tip_msg){
            default_tip_msg = tip_msg
        }
        let { code, msg, data } = resp.data;
        if (code == 0) {
            if(default_tip_msg){
                msg_success(default_tip_msg)
            }           
            return data
        }
        msg_error(msg)
    } catch (error) {
        msg_error(error.message)
        console.log(error)
    }
}



export default send_req
```





#### 插件和扩展

plugins/index.js

```javascript

import Antd from 'ant-design-vue';
// 3.0 +
// import 'ant-design-vue/dist/antd.css'; 
// 4.0 +
import 'ant-design-vue/dist/reset.css';
import router from '@/router'
import * as antIcons from '@ant-design/icons-vue'

/**
 * 插件集
 * @type {import('vue').plugin[]}
*/

const plugins = [
    router, Antd
]

/**
 * 注册
 * @param {import('vue').App} app 
 * @returns 
 * 
 */

const usePlugins = app => {
    plugins.forEach(app.use, app)
    Object.keys(antIcons).forEach(key => {
        app.component(key, antIcons[key])
    })
    //全局设置
    app.config.globalProperties.$antIcons = antIcons
    app.config.globalProperties.$router = router
}




export default usePlugins
```



##### `main.js` 注册

```javascript
import { createApp } from 'vue'
import App from './App.vue'
import usePlugins from './plugins'

const app = createApp(App)

usePlugins(app)

app.mount('#app')

```

