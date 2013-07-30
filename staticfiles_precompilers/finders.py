import os

from django.conf import settings
from django.contrib.staticfiles.finders import FileSystemFinder

import envoy


class PrecompilerFinder(FileSystemFinder):

    def find_location(self, root, path, prefix=None):
        file_name, file_ext = os.path.splitext(path)

        if file_ext in settings.STATICFILES_PRECOMPILERS:
            handler = settings.STATICFILES_PRECOMPILERS[file_ext]
            new_path = handler[1].format(file_name=file_name)
            
            infile = os.path.normpath(os.path.join(root, path))
            outfile = os.path.normpath(os.path.join(root, new_path))

            envoy.run(handler[0].format(infile=infile, outfile=outfile))  

            path = new_path
        return super(PrecompilerFinder, self).find_location(root, path, prefix=prefix)

    def list(self, ignore_patterns):
        for path, storage in super(PrecompilerFinder, self).list(ignore_patterns):
            file_name, file_ext = os.path.splitext(path)

            if file_ext in settings.STATICFILES_PRECOMPILERS:
                handler = settings.STATICFILES_PRECOMPILERS[file_ext]
                new_path = handler[1].format(file_name=file_name)
                infile = storage.path(path)
                outfile = storage.path(new_path)
                envoy.run(handler[0].format(infile=infile, outfile=outfile))                
                yield new_path, storage
            else:
                yield path, storage