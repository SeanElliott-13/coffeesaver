import React, { useState } from 'react';
import { CirclePlus, Coffee, MapPin, Award, User, Settings, Navigation, Search, Trophy, Bell, Moon, Smartphone, Heart, LogOut, HelpCircle, ChevronRight } from 'lucide-react';

const EspressoEarningsApp = () => {
  const [activeTab, setActiveTab] = useState('settings');
  
  // Sample user data with updated coffee shop names and user
  const userData = {
    name: "Sean",
    username: "SeanElliott",
    steps: 8743,
    dailyGoal: 10000,
    rewards: [
      { id: 1, shop: "Helix", discount: "15% off", stepsNeeded: 8000, earned: true },
      { id: 2, shop: "The Tram Cafe", discount: "Free upsize", stepsNeeded: 10000, earned: false },
      { id: 3, shop: "Starbucks", discount: "Buy 1 Get 1", stepsNeeded: 15000, earned: false }
    ],
    nearbyShops: [
      { id: 1, name: "Helix", distance: "0.3 miles", address: "DCU Business School" },
      { id: 2, name: "The Tram Cafe", distance: "0.5 miles", address: "DCU Library" },
      { id: 3, name: "Starbucks", distance: "0.8 miles", address: "DCU Student Centre" }
    ]
  };
  
  // Sample leaderboard data with updated names
  const leaderboardData = [
    { id: 1, name: "RachelDeehan4", steps: 12467, avatar: "RD", rank: 1 },
    { id: 2, name: "SeanElliott", steps: 8743, avatar: "SE", rank: 2, isUser: true },
    { id: 3, name: "Hannah Moreau", steps: 7856, avatar: "HM", rank: 3 },
    { id: 4, name: "Emma McMenamin", steps: 6934, avatar: "EM", rank: 4 }
  ];
  
  // Sample settings options
  const settingsOptions = [
    {
      category: "Account",
      items: [
        { id: "profile", label: "Profile", icon: <User size={20} />, rightElement: <ChevronRight size={18} /> },
        { id: "notifications", label: "Notifications", icon: <Bell size={20} />, rightElement: <div className="h-5 w-10 bg-green-600 rounded-full flex items-center pl-1"><div className="h-4 w-4 bg-white rounded-full"></div></div> },
        { id: "dailyGoal", label: "Daily Step Goal", icon: <Award size={20} />, rightElement: <span className="text-gray-700">10,000</span> }
      ]
    },
    {
      category: "App Settings",
      items: [
        { id: "darkMode", label: "Dark Mode", icon: <Moon size={20} />, rightElement: <div className="h-5 w-10 bg-gray-300 rounded-full flex items-center justify-end pr-1"><div className="h-4 w-4 bg-white rounded-full"></div></div> },
        { id: "mapDefault", label: "Default Map View", icon: <MapPin size={20} />, rightElement: <span className="text-gray-700">DCU Campus</span> },
        { id: "connected", label: "Connected Devices", icon: <Smartphone size={20} />, rightElement: <span className="text-gray-700">Fitbit Versa</span> }
      ]
    },
    {
      category: "Health Sync",
      items: [
        { id: "healthApp", label: "Connect Health App", icon: <Heart size={20} />, rightElement: <div className="h-5 w-10 bg-green-600 rounded-full flex items-center pl-1"><div className="h-4 w-4 bg-white rounded-full"></div></div> },
        { id: "dataPrivacy", label: "Data Privacy", icon: <HelpCircle size={20} />, rightElement: <ChevronRight size={18} /> }
      ]
    },
    {
      category: "Support & About",
      items: [
        { id: "help", label: "Help & FAQs", icon: <HelpCircle size={20} />, rightElement: <ChevronRight size={18} /> },
        { id: "about", label: "About", icon: <Coffee size={20} />, rightElement: <span className="text-gray-700">v2.1.3</span> },
        { id: "logout", label: "Log Out", icon: <LogOut size={20} />, rightElement: null, danger: true }
      ]
    }
  ];
  
  // Progress calculation
  const progress = (userData.steps / userData.dailyGoal) * 100;
  
  const renderHomeScreen = () => (
    <div className="p-4 space-y-6">
      {/* Steps Progress */}
      <div className="bg-green-50 rounded-xl p-6 shadow-sm">
        <h2 className="text-lg font-medium text-green-900">Today's Steps</h2>
        <div className="mt-2 flex items-end">
          <div className="text-4xl font-bold text-green-800">{userData.steps.toLocaleString()}</div>
          <div className="ml-2 text-green-600 pb-1">/ {userData.dailyGoal.toLocaleString()} steps</div>
        </div>
        
        {/* Progress bar */}
        <div className="mt-4 h-4 bg-green-200 rounded-full overflow-hidden">
          <div 
            className="h-full bg-green-600 rounded-full"
            style={{ width: `${Math.min(progress, 100)}%` }}
          ></div>
        </div>
        
        <div className="mt-2 text-sm text-green-700">
          {progress < 100 
            ? `${(userData.dailyGoal - userData.steps).toLocaleString()} more steps to reach your daily goal!` 
            : "Daily goal reached! Keep going for bonus rewards!"}
        </div>
      </div>
      
      {/* Available Rewards */}
      <div className="mt-6">
        <h2 className="text-lg font-medium mb-3">Your Rewards</h2>
        <div className="space-y-3">
          {userData.rewards.map(reward => (
            <div key={reward.id} className={`p-4 rounded-lg shadow-sm border flex justify-between items-center ${reward.earned ? 'bg-green-50 border-green-200' : 'bg-white border-gray-200'}`}>
              <div>
                <div className="font-medium">{reward.shop}</div>
                <div className="text-lg font-bold">{reward.discount}</div>
                <div className="text-sm text-gray-600">{reward.stepsNeeded.toLocaleString()} steps needed</div>
              </div>
              {reward.earned ? (
                <div className="bg-green-600 text-white px-3 py-1 rounded-full text-sm font-medium">
                  Ready to use
                </div>
              ) : (
                <div className="text-green-600 text-sm font-medium">
                  {Math.round((userData.steps/reward.stepsNeeded)*100)}% progress
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
      
      {/* Nearby Coffee Shops */}
      <div className="mt-6">
        <h2 className="text-lg font-medium mb-3">Nearby Coffee Shops</h2>
        <div className="space-y-3">
          {userData.nearbyShops.map(shop => (
            <div key={shop.id} className="p-4 rounded-lg shadow-sm border bg-white flex justify-between items-center">
              <div>
                <div className="font-medium">{shop.name}</div>
                <div className="text-sm text-gray-600">{shop.address}</div>
              </div>
              <div className="text-green-600 font-medium">
                {shop.distance}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
  
  const renderMapScreen = () => (
    <div className="flex flex-col h-full">
      {/* Map Search Bar */}
      <div className="p-4 border-b">
        <div className="flex items-center bg-gray-100 rounded-lg px-3 py-2">
          <Search size={18} className="text-gray-500 mr-2" />
          <input 
            type="text" 
            placeholder="Search DCU campus..." 
            className="bg-transparent flex-1 outline-none text-gray-800"
            defaultValue="DCU Campus"
          />
        </div>
      </div>
      
      {/* DCU Map */}
      <div className="relative flex-1 bg-gray-100">
        {/* SVG Map of DCU Campus */}
        <svg viewBox="0 0 800 600" className="w-full h-full">
          {/* Campus outline */}
          <rect x="50" y="50" width="700" height="500" fill="#e5e7eb" stroke="#9ca3af" strokeWidth="2" />
          
          {/* Main roads */}
          <path d="M50,300 H750" stroke="#9ca3af" strokeWidth="8" />
          <path d="M400,50 V550" stroke="#9ca3af" strokeWidth="8" />
          
          {/* Building blocks */}
          {/* DCU Business School - Helix */}
          <rect x="100" y="100" width="200" height="150" fill="#d1d5db" stroke="#6b7280" strokeWidth="2" />
          <text x="120" y="180" fontSize="16" fill="#374151">Business School</text>
          <text x="120" y="140" fontSize="14" fontWeight="bold" fill="#374151">Helix</text>
          <circle cx="150" cy="150" r="10" fill="#ef4444" stroke="#b91c1c" strokeWidth="2" />
          
          {/* DCU Library - The Tram Cafe */}
          <rect x="450" y="100" width="250" height="150" fill="#d1d5db" stroke="#6b7280" strokeWidth="2" />
          <text x="520" y="180" fontSize="16" fill="#374151">Library</text>
          <text x="520" y="140" fontSize="14" fontWeight="bold" fill="#374151">The Tram Cafe</text>
          <circle cx="500" cy="150" r="10" fill="#ef4444" stroke="#b91c1c" strokeWidth="2" />
          
          {/* Student Centre - Starbucks */}
          <rect x="450" y="350" width="250" height="150" fill="#d1d5db" stroke="#6b7280" strokeWidth="2" />
          <text x="500" y="430" fontSize="16" fill="#374151">Student Centre</text>
          <text x="500" y="390" fontSize="14" fontWeight="bold" fill="#374151">Starbucks</text>
          <circle cx="500" cy="400" r="10" fill="#ef4444" stroke="#b91c1c" strokeWidth="2" />
          
          {/* Engineering Building */}
          <rect x="100" y="350" width="200" height="150" fill="#d1d5db" stroke="#6b7280" strokeWidth="2" />
          <text x="120" y="430" fontSize="16" fill="#374151">Engineering</text>
          
          {/* User location */}
          <circle cx="300" cy="300" r="12" fill="#3b82f6" stroke="#ffffff" strokeWidth="3" />
          <circle cx="300" cy="300" r="30" fill="#3b82f6" fillOpacity="0.2" />
          
          {/* Coffee shop indicators */}
          <circle cx="150" cy="150" r="15" fill="#16a34a" fillOpacity="0.7" stroke="#ffffff" strokeWidth="2" />
          <text x="140" y="155" fill="#ffffff" fontSize="16" fontWeight="bold">‚òï</text>
          
          <circle cx="500" cy="150" r="15" fill="#16a34a" fillOpacity="0.7" stroke="#ffffff" strokeWidth="2" />
          <text x="490" y="155" fill="#ffffff" fontSize="16" fontWeight="bold">‚òï</text>
          
          <circle cx="500" cy="400" r="15" fill="#16a34a" fillOpacity="0.7" stroke="#ffffff" strokeWidth="2" />
          <text x="490" y="405" fill="#ffffff" fontSize="16" fontWeight="bold">‚òï</text>
        </svg>
        
        {/* Map controls */}
        <div className="absolute bottom-6 right-6 bg-white rounded-full p-3 shadow-lg">
          <Navigation size={24} className="text-gray-700" />
        </div>
        
        {/* Zoom controls */}
        <div className="absolute top-6 right-6 bg-white rounded-lg shadow-lg">
          <button className="p-2 border-b border-gray-200 flex items-center justify-center">
            <span className="text-xl font-bold">+</span>
          </button>
          <button className="p-2 flex items-center justify-center">
            <span className="text-xl font-bold">‚àí</span>
          </button>
        </div>
      </div>
      
      {/* Nearby coffee shops list */}
      <div className="bg-white border-t border-gray-200 p-4">
        <h3 className="text-md font-medium mb-3">Coffee Shops on Campus</h3>
        <div className="space-y-2">
          {userData.nearbyShops.map(shop => (
            <div key={shop.id} className="flex items-center justify-between py-2 border-b border-gray-100">
              <div className="flex items-center">
                <div className="h-8 w-8 rounded-full bg-green-100 flex items-center justify-center mr-3">
                  <Coffee size={16} className="text-green-800" />
                </div>
                <div>
                  <div className="font-medium">{shop.name}</div>
                  <div className="text-xs text-gray-500">{shop.address}</div>
                </div>
              </div>
              <div className="text-green-600 text-sm font-medium">{shop.distance}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
  
  const renderLeaderboardScreen = () => (
    <div className="flex flex-col h-full">
      <div className="p-4 border-b bg-green-50">
        <h3 className="text-lg font-bold text-green-900 text-center">Step Challenge Leaderboard</h3>
        <p className="text-sm text-green-700 text-center mt-1">Today's Top Walkers</p>
      </div>
      
      {/* Podium view */}
      <div className="bg-green-50 p-4 flex justify-center items-end space-x-4">
        {/* Second place */}
        <div className="flex flex-col items-center">
          <div className="w-16 h-16 bg-green-200 rounded-full mb-2 flex items-center justify-center border-2 border-green-300">
            <span className="text-xl font-bold text-green-800">SE</span>
          </div>
          <div className="bg-green-100 w-20 h-28 flex items-center justify-center rounded-t-lg border-2 border-b-0 border-green-300">
            <span className="text-2xl font-bold text-green-700">2</span>
          </div>
          <p className="text-sm font-medium mt-1 text-green-800">You</p>
          <p className="text-xs font-bold text-green-900">{userData.steps.toLocaleString()} steps</p>
        </div>
        
        {/* First place */}
        <div className="flex flex-col items-center">
          <div className="w-20 h-20 bg-green-200 rounded-full mb-2 flex items-center justify-center border-2 border-green-400">
            <Trophy size={36} className="text-green-600" />
          </div>
          <div className="bg-green-100 w-24 h-36 flex items-center justify-center rounded-t-lg border-2 border-b-0 border-green-400">
            <span className="text-3xl font-bold text-green-700">1</span>
          </div>
          <p className="text-sm font-medium mt-1 text-green-800">{leaderboardData[0].name}</p>
          <p className="text-xs font-bold text-green-900">{leaderboardData[0].steps.toLocaleString()} steps</p>
        </div>
        
        {/* Third place */}
        <div className="flex flex-col items-center">
          <div className="w-16 h-16 bg-green-200 rounded-full mb-2 flex items-center justify-center border-2 border-green-300">
            <span className="text-xl font-bold text-green-800">HM</span>
          </div>
          <div className="bg-green-100 w-20 h-20 flex items-center justify-center rounded-t-lg border-2 border-b-0 border-green-300">
            <span className="text-2xl font-bold text-green-700">3</span>
          </div>
          <p className="text-sm font-medium mt-1 text-green-800">{leaderboardData[2].name}</p>
          <p className="text-xs font-bold text-green-900">{leaderboardData[2].steps.toLocaleString()} steps</p>
        </div>
      </div>
      
      {/* Full leaderboard list */}
      <div className="flex-1 bg-white p-4 overflow-y-auto">
        <h3 className="font-medium text-gray-700 mb-3">Full Leaderboard</h3>
        <div className="space-y-3">
          {leaderboardData.map((user) => (
            <div 
              key={user.id} 
              className={`p-3 rounded-lg flex items-center ${user.isUser ? 'bg-green-50 border border-green-200' : 'bg-white border border-gray-200'}`}
            >
              <div className="w-8 h-8 flex items-center justify-center mr-2">
                <span className="font-bold text-lg text-gray-700">{user.rank}</span>
              </div>
              <div className={`w-10 h-10 rounded-full flex items-center justify-center mr-3 ${user.isUser ? 'bg-green-200 text-green-800' : 'bg-gray-200 text-gray-700'}`}>
                <span className="font-bold">{user.avatar}</span>
              </div>
              <div className="flex-1">
                <div className={`font-medium ${user.isUser ? 'text-green-800' : 'text-gray-800'}`}>
                  {user.name} {user.isUser && <span className="text-xs ml-1">(You)</span>}
                </div>
                <div className="text-sm text-gray-500">
                  {user.steps.toLocaleString()} steps today
                </div>
              </div>
              {user.rank === 1 && (
                <div className="ml-2">
                  <Trophy size={20} className="text-green-500" />
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
      
      {/* Motivational message */}
      <div className="p-4 bg-white border-t border-gray-200">
        <div className="bg-green-50 p-3 rounded-lg">
          <p className="text-sm text-green-800 text-center">
            You're just <span className="font-bold">{(leaderboardData[0].steps - userData.steps).toLocaleString()}</span> steps away from taking the lead!
          </p>
        </div>
      </div>
    </div>
  );
  
  const renderSettingsScreen = () => (
    <div className="flex flex-col h-full bg-gray-50">
      {/* Profile summary */}
      <div className="bg-green-800 text-white px-4 py-6">
        <div className="flex items-center">
          <div className="w-16 h-16 rounded-full bg-green-700 flex items-center justify-center mr-4">
            <span className="text-xl font-bold">SE</span>
          </div>
          <div>
            <h3 className="text-xl font-bold">{userData.name}</h3>
            <p className="text-green-200">@{userData.username}</p>
            <div className="flex items-center mt-1">
              <span className="text-xs bg-green-700 px-2 py-1 rounded-full">Coffee Enthusiast</span>
              <span className="text-xs ml-2">Member since 2023</span>
            </div>
          </div>
        </div>
      </div>
      
      {/* Settings options */}
      <div className="flex-1 p-4 space-y-6 overflow-y-auto">
        {settingsOptions.map((section) => (
          <div key={section.category} className="bg-white rounded-lg shadow-sm overflow-hidden">
            <h3 className="px-4 py-2 bg-gray-50 text-gray-700 font-medium border-b">{section.category}</h3>
            <div>
              {section.items.map((item) => (
                <div 
                  key={item.id} 
                  className={`flex items-center justify-between px-4 py-3 border-b last:border-b-0 ${item.danger ? 'text-red-600' : 'text-gray-800'}`}
                >
                  <div className="flex items-center">
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center mr-3 ${item.danger ? 'bg-red-100' : 'bg-green-100'}`}>
                      {item.icon}
                    </div>
                    <span className="font-medium">{item.label}</span>
                  </div>
                  <div className="text-gray-400">
                    {item.rightElement}
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
      
      {/* App version footer */}
      <div className="p-4 border-t bg-white">
        <p className="text-xs text-center text-gray-500">
          Espresso Earnings v2.1.3 ‚Ä¢ ¬© 2025 Stride & Sip Inc.
        </p>
      </div>
    </div>
  );
  
  return (
    <div className="max-w-md mx-auto bg-white h-screen flex flex-col">
      {/* App Header - Only show on non-settings screens */}
      {activeTab !== 'settings' && (
        <div className="bg-green-800 text-white px-4 py-6">
          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-xl font-bold">Espresso Earnings</h1>
              <p className="text-green-200">Walk more, save more!</p>
            </div>
            <div className="h-10 w-10 rounded-full bg-green-700 flex items-center justify-center">
              <User size={20} />
            </div>
          </div>
        </div>
      )}
      
      {/* Main Content */}
      <div className="flex-1 overflow-y-auto">
        {activeTab === 'home' && renderHomeScreen()}
        {activeTab === 'map' && renderMapScreen()}
        {activeTab === 'leaderboard' && renderLeaderboardScreen()}
        {activeTab === 'settings' && renderSettingsScreen()}
      </div>
      
      {/* Bottom Navigation */}
      <div className="border-t border-gray-200 bg-white">
        <div className="flex justify-around py-3">
          <button 
            className={`flex flex-col items-center px-4 ${activeTab === 'home' ? 'text-green-800' : 'text-gray-500'}`}
            onClick={() => setActiveTab('home')}
          >
            <Coffee size={24} />
            <span className="text-xs mt-1">Home</span>
          </button>
          
          <button 
            className={`flex flex-col items-center px-4 ${activeTab === 'map' ? 'text-green-800' : 'text-gray-500'}`}
            onClick={() => setActiveTab('map')}
          >
            <MapPin size={24} />
            <span className="text-xs mt-1">Map</span>
          </button>
          
          <button 
            className={`flex flex-col items-center px-4 ${activeTab === 'leaderboard' ? 'text-green-800' : 'text-gray-500'}`}
            onClick={() => setActiveTab('leaderboard')}
          >
            <Trophy size={24} />
            <span className="text-xs mt-1">Leaderboard</span>
          </button>
          
          <button 
            className={`flex flex-col items-center px-4 ${activeTab === 'settings' ? 'text-green-800' : 'text-gray-500'}`}
            onClick={() => setActiveTab('settings')}
          >
            <Settings size={24} />
            <span className="text-xs mt-1">Settings</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default EspressoEarningsApp;