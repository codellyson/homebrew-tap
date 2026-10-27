cask "justdb" do
  version "0.2.5"
  sha256 "ec2523fef19eb710da2e5b0278ba76a523687db212ad8bf6c9951711a586b636"

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
