const app = getApp()

Page({
  data: {
    details: {}
  },

  onLoad: function() {
    var me = this;
    var serverUrl = app.serverUrl
    me.setData({
      id: wx.getStorageSync('id'),
      platform: wx.getStorageSync('platform')
    })
    if (wx.getStorageSync('vehicles') == null || wx.getStorageSync('vehicles') == undefined || wx.getStorageSync('vehicles').length == 0) {
      wx.showToast({
        title: '查询中。。',
        icon:'none',
        duration:2000
      })
      wx.request({
        url: serverUrl+'/get_vehicles',
        method: 'GET',
        data: {
          id: me.data.id,
          platform: me.data.platform
        },
        success: function (result) {
          me.setData({
            details: result.data
          });
          wx.setStorageSync('vehicles', result.data);
        }
      })
    } else {
      me.setData({
        details: wx.getStorageSync('vehicles')
      });
    }
  },

  getDetail: function () {
    wx.redirectTo({
      url: '../detail/detail'
    })
  },
  
  getWeapons: function () {
    wx.redirectTo({
      url: '../weapon/weapon'
    })
  },

  toIndex: function() {
    wx.navigateTo({
      url: '../index/index',
    })
  },

  aboutMe: function() {
    wx.navigateTo({
      url: '../aboutme/aboutme',
    })
  }
})