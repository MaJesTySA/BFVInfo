//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    details: [],
    platform_array: ['origin', 'psn', 'xbox']
  },

  onLoad: function(e) {
    if (e.msg == '404') {
      wx.showToast({
        title: '账户不存在！请重新输入',
        icon: 'none',
        duration: 2000
      })
    } else if (e.msg == '500') {
      wx.showToast({
        title: '服务器错误！请稍后重试',
        icon: 'none',
        duration: 2000
      })
    }
  },

  getDetail: function(e) {
    var me = this;
    var id = e.detail.value.id;
    if ((id != null && id.length > 0) && me.data.platform != null) {
      wx.redirectTo({
        url: '../detail/detail?platform=' + me.data.platform + '&id=' + id,
      })
    } else {
      wx.showToast({
        title: '平台或者ID不能为空',
        duration: 1500,
        icon: 'none'
      })
    }
  },

  pickerChange: function(e) {
    var me = this;
    var index = e.detail.value;
    me.setData({
      platform: me.data.platform_array[index]
    })
  },

})