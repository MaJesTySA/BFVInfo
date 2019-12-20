const app = getApp()

Page({
  data: {
    details: []
  },

  onLoad: function() {
    var me = this;
    me.setData({
      'details':wx.getStorageSync('dataStorage').data.weapons,
      'id':wx.getStorageSync('id'),
      'platform':wx.getStorageSync('platform')
    })
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