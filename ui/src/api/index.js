/**
 * @description API统一管理
 * @author 凉风有信、
 */

import request from './../utils/request'
export default {
  loginApi(params) {
    return request({
      url: '/accounts/login',
      method: 'post',
      data: params
      // mock: true
    })
  },
  registerApi(params) {
    return request({
      url: '/accounts/register',
      method: 'post',
      data: params
      // mock: true
    })
  },
  uploadAvatar() {
    
  }
}