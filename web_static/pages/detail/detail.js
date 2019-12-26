const app = getApp()

Page({
  data: {
    details: []
  },

  onLoad: function(e) {
    var me = this
    //e.id不为空，则表示从index页面传过来，需要重新查询。
    if (e.id != null || e.id != undefined) {
      me.setData({
        id: e.id,
        platform: e.platform
      })
      wx.showToast({
        title: '查询中。。',
        duration: 10000,
        icon: 'loading'
      })
      wx.request({
        url: 'https://app.majestysa.site/get_info',
        method: 'GET',
        data: {
          id: me.data.id,
          platform: me.data.platform
        },
        success: function(result) {
          if (result.data.error == '404') {
            wx.redirectTo({
              url: '../index/index?msg=' + result.data.error,
            })
          } else if (result.data.error == '500') {
            wx.redirectTo({
              url: '../index/index?msg=' + result.data.error,
            })
          } else if (result.data.error == '400') {
            wx.redirectTo({
              url: '../index/index?msg=' + result.data.error,
            })
          } else {
            me.setData({
              details: result
            });
            wx.setStorageSync('dataStorage', result);
            wx.setStorageSync('id', me.data.id)
            wx.setStorageSync('platform', me.data.platform)
          }
        }
      })
      //如果e为空，则表示已经查询过，直接从缓存中取
    } else {
      me.setData({
        details: wx.getStorageSync('dataStorage'),
        id: wx.getStorageSync('id'),
        platform: wx.getStorageSync('platform')
      })
    }
  },

  getWeapons: function() {
    wx.redirectTo({
      url: '../weapon/weapon'
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
  }

})