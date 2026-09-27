cask "justdb" do
  version "0.2.4"
  sha256 "c19ab816184b5fe44f8297a8deec538b836f5f7fd24239b035f350a2174efadc"

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
