const app = getApp()

Page({
  data: {
    details: []
  },

  onLoad: function(e) {
    var me = this;
    me.setData({
      'details': wx.getStorageSync('dataStorage').data.vehicles,
      'id': wx.getStorageSync('id'),
      'platform': wx.getStorageSync('platform')
    })
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