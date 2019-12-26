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
    if (wx.getStorageSync('weapons') == null || wx.getStorageSync('weapons') == undefined || wx.getStorageSync('weapons').length == 0) {
      wx.showToast({
        title: '查询中。。',
        icon: 'none',
        duration: 2000
      })
      wx.request({
        url: serverUrl+'/get_weapons',
        method: 'GET',
        data: {
          id: me.data.id,
          platform: me.data.platform
        },
        success: function(result) {
          me.setData({
            details: result.data
          });
          wx.setStorageSync('weapons', result.data);
        }
      })
    } else {
      me.setData({
        details: wx.getStorageSync('weapons')
      });
    }
  },

  getDetail: function() {
    wx.redirectTo({
      url: '../detail/detail'
    })
  },

  getVehicles: function() {
    wx.redirectTo({
      url: '../vehicle/vehicle'
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
  },

})