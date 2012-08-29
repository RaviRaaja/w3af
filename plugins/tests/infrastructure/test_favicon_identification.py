'''
test_favicon_identification.py

Copyright 2012 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''

from ..helper import PluginTest, PluginConfig


class TestFaviconIdentification(PluginTest):
    
    favicon_url = 'http://moth/'
    no_favicon_url = 'http://wordpress/'
    
    _run_configs = {
        'cfg': {
                'target': None,
                'plugins': {'infrastructure': (PluginConfig('favicon_identification'),)}
                }
        }
    
    def test_no_favicon_identification_http(self):
        cfg = self._run_configs['cfg']
        self._scan(self.no_favicon_url, cfg['plugins'])
        
        infos = self.kb.getData('favicon_identification', 'info')
        self.assertEqual( len(infos), 0, infos)
    
    def test_favicon_identification_http(self):
        cfg = self._run_configs['cfg']
        self._scan(self.favicon_url, cfg['plugins'])
        
        infos = self.kb.getData('favicon_identification', 'info')
        self.assertEqual( len(infos), 1, infos)
        
        info = infos[0]
        self.assertEqual( info.getName(), 'Favicon identification')
        self.assertTrue('tomcat' in info.getDesc().lower(), info.getDesc())
        
        