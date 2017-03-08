require 'autoproj/gitorious'
Autoproj.gitorious_server_configuration('GITHUB', 'github.com', :http_url => 'https://github.com')

Autoproj.gitorious_server_configuration('DFKIGIT', 'git.hb.dfki.de', :fallback_to_http => false, default: 'ssh,ssh', disabled_methods: 'http,git')
