cask "justdb" do
  version "0.2.3"
  sha256 "9a2e7951f26e421fe8ed4181533add8e8b0c6798061bc099b41596ede3ea8f19"

  url "https://github.com/codellyson/justdb/releases/download/v#{version}/JustDB_#{version}_universal.dmg"
  name "JustDB"
  desc "Desktop database client for browsing, querying, and editing data"
  homepage "https://justdb.kreativekorna.com/"

  livecheck do
    url :url
    strategy :github_latest
  end

  app "JustDB.app"
end
